from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from backend.src.config import settings
from backend.src.logger import logger


mail_settings = settings.mail

mail_config = ConnectionConfig(
    MAIL_USERNAME=mail_settings.MAIL_USERNAME,
    MAIL_PASSWORD=mail_settings.MAIL_PASSWORD,
    MAIL_FROM=mail_settings.MAIL_FROM,
    MAIL_PORT=mail_settings.MAIL_PORT,
    MAIL_SERVER=mail_settings.MAIL_SERVER,
    MAIL_SSL_TLS=bool(mail_settings.MAIL_SSL),
    USE_CREDENTIALS=True
)

async def send_email(subject: str, recipients: list[str], body: str):
    logger.info(f"Sending email with subject {subject} to {recipients}")
    message = MessageSchema(
        subject=subject,
        recipients=recipients,
        body=body,
        subtype="html"
    )

    fm = FastMail(mail_config)
    await fm.send_message(message)
