import pytest
import pandas as pd
from pinch.analysis import classify_streams


def test_classify_streams():
    df = pd.DataFrame({
        "Supply Temperature": [10, 10, 10],
        "Target Temperature": [8, 8, 12],
    })
    correct = pd.Series({"Condition": ["HOT", "HOT", "COLD"]})
    assert classify_streams(df).equals(correct)