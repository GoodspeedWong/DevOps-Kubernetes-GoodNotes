#!/usr/bin/env python3.12

import sys
import json
import time
import statistics
import random
import asyncio
import aiohttp

HOSTS = ["foo.localhost", "bar.localhost"]
URL = "http://127.0.0.1:8080/"

async def fetch(session, host):
    start = time.perf_counter()
    try:
        async with session.get(URL, headers={"Host": host}) as resp:
            await resp.text()
            return time.perf_counter() - start, resp.status
    except Exception:
        return None, None

async def run_load(total: int, concurrency: int):
    results = []
    sem = asyncio.Semaphore(concurrency)
    async with aiohttp.ClientSession() as session:
        async def worker():
            async with sem:
                host = random.choice(HOSTS)
                duration, status = await fetch(session, host)
                results.append((host, duration, status))
        tasks = [asyncio.create_task(worker()) for _ in range(total)]
        await asyncio.gather(*tasks)
    durations = [d for _, d, s in results if d is not None]
    failed = [1 for _, d, s in results if s != 200 or d is None]
    succeeded = len(results) - len(failed)

    per_host = {h: {"requests": 0, "success": 0, "failed": 0, "durations": []} for h in HOSTS}
    for host, duration, status in results:
        data = per_host[host]
        data["requests"] += 1
        if duration is not None:
            data["durations"].append(duration)
        if status == 200 and duration is not None:
            data["success"] += 1
        else:
            data["failed"] += 1

    stats = {
        "requests": len(results),
        "success": succeeded,
        "failed_percent": (len(failed) / len(results)) * 100 if results else 0,
        "hosts": {},
    }

    if durations:
        qs = statistics.quantiles(durations, n=100)
        stats.update(
            {
                "avg_duration": statistics.mean(durations),
                "p90": round(qs[89], 4),
                "p95": round(qs[94], 4),
                "p99": round(qs[98], 4),
                "rps": len(durations) / sum(durations),
            }
        )

    for host, data in per_host.items():
        host_stats = {
            "requests": data["requests"],
            "success": data["success"],
            "failed_percent": (data["failed"] / data["requests"]) * 100 if data["requests"] else 0,
        }
        if data["durations"]:
            qs = statistics.quantiles(data["durations"], n=100)
            host_stats.update(
                {
                    "avg_duration": statistics.mean(data["durations"]),
                    "p90": round(qs[89], 4),
                    "p95": round(qs[94], 4),
                    "p99": round(qs[98], 4),
                    "rps": len(data["durations"]) / sum(data["durations"]),
                }
            )
        stats["hosts"][host] = host_stats

    return stats

if __name__ == "__main__":
    total = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    concurrency = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    summary = asyncio.run(run_load(total, concurrency))
    print(json.dumps(summary, indent=2))
    