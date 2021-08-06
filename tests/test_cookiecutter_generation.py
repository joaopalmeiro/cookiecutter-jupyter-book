def test_project_generation(cookies):
    result = cookies.bake(extra_context={"book_name": "test-book"})

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "test_book"
    assert result.project_path.is_dir()
