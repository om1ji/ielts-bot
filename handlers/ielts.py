from handlers.common import *

router = Router()


@router.message(F.text == buttons.get_test.text)
async def move_to_main_menu(message: Message):
    raise NotImplementedError
