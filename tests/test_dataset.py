def test_train_data():
    try:
        import os.path

        file_exists = os.path.exists("datasets/housing.csv")
    except Exception as e:
        assert False, f"Error: {e}. Datasets not downloaded."


if __name__ == "__main__":
    test_train_data()

