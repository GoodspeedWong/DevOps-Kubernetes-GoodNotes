# train.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

MODEL_PATH = "model.joblib"

def train():
    iris = load_iris()
    X = iris.data
    y = iris.target

    # 用 Pipeline 把 scaler + model 串起来，方便部署时只调用 predict
    clf = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("logreg", LogisticRegression(max_iter=200)),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    clf.fit(X_train, y_train)
    acc = clf.score(X_test, y_test)
    print(f"Test accuracy: {acc:.4f}")

    joblib.dump(clf, MODEL_PATH)
    print(f"Saved model to {MODEL_PATH}")

if __name__ == "__main__":
    train()