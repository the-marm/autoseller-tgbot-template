from telegram_bot.config import (
    CommonConfig,
    Config,
    NovaPoshtaConfig,
    PostgresConfig,
    RedisConfig,
    WebhookConfig,
)


def create_config() -> Config:
    return Config(
        common=CommonConfig(),  # pyright: ignore[reportCallIssue]
        postgres=PostgresConfig(),  # pyright: ignore[reportCallIssue]
        nova_poshta=NovaPoshtaConfig(),  # pyright: ignore[reportCallIssue]
        redis=RedisConfig(),  # pyright: ignore[reportCallIssue]
        webhook=WebhookConfig(),  # pyright: ignore[reportCallIssue]
    )
