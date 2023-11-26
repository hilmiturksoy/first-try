from plyer import notification

notification_title = "Öncelikli Bildiriniz Var!"
notification_message = "Mesajı Dikkate Aldırınız İçin Teşekkürler"

notification.notify(
    title=notification_title,
    message=notification_message,
    app_icon=None,
    timeout=3,
    toast=False
)