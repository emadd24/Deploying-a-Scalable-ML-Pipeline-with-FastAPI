import pytest
import numpy as np
from sklearn.ensemble import RandomForestClassifier

from ml.model import train_model, compute_model_metrics


# Test 1: model trains correctly
def test_train_model():
    X = np.array([[1, 2], [3, 4], [5, 6]])
    y = np.array([0, 1, 0])

    model = train_model(X, y)

    assert isinstance(model, RandomForestClassifier)


# Test 2: predictions match input size
def test_inference_length():
    X = np.array([[1, 2], [3, 4], [5, 6]])
    y = np.array([0, 1, 0])

    model = train_model(X, y)
    preds = model.predict(X)

    assert len(preds) == len(y)


# Test 3: metrics are valid numbers
def test_compute_model_metrics():
    y = np.array([1, 0, 1, 1])
    preds = np.array([1, 0, 0, 1])

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= fbeta <= 1