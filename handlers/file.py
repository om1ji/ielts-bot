from handlers.common import *

router = Router()


@router.message(F.document)
async def upload_file(message: Message):
    file_id = message.document.file_id
    file_type = message.document.mime_type
    category = message.caption

    db.insert_file(file_id, file_type, category)
    await message.answer("Файл успешно загружен!")
