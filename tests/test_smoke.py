import rag_failure_lab


def test_package_imports_and_has_version() -> None:
    assert rag_failure_lab.hello() == "Hello from rag-failure-lab!"
