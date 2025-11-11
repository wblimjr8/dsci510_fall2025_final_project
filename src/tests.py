from load import load_cms_data

def test_cms_data_loads():
    # Ensure that CMS API data returns a non-empty dataset
    df = load_cms_data()
    assert not df.empty, "CMS data should not be empty"
    print("Test passed: CMS data successfully loaded with", len(df), "rows.")

if __name__ == "__main__":
    test_cms_data_loads()