from types import SimpleNamespace
from unittest.mock import patch

from app.ask import ask


def test_ask_prints_input_and_output_token_counts(capsys):
    response = SimpleNamespace(
        text="回答",
        usage_metadata=SimpleNamespace(
            prompt_token_count=12,
            candidates_token_count=7,
        ),
    )
    client = SimpleNamespace(
        models=SimpleNamespace(generate_content=lambda **_: response),
    )

    with patch("app.ask.genai.Client", return_value=client), patch(
        "app.ask.get_api_key", return_value="test-key"
    ):
        assert ask("質問") == "回答"

    assert "[usage] 入力: 12, 出力: 7" in capsys.readouterr().out
