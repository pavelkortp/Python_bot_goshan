from loader import dp
from aiogram.types import ContentType, Message, InputFile, MediaGroup
from keyboards.inline import ikb_menu
from filters import IsPrivate

@dp.message_handler(IsPrivate(), content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(IsPrivate(), content_types=ContentType.VIDEO)
async def send_video_file_id(message: Message):
    await message.reply(message.video.file_id)


@dp.message_handler(text = '/photo')
async def send_photo(message: Message):
    photo_file_id = 'AgACAgIAAxkBAAIFFmMWPNXiZ1nGbdA8fe1VfPVmfVCoAAKMxDEb1lS4SPGrpPRmMkBBAQADAgADeQADKQQ'
    photo_bytes = InputFile(path_or_bytesio='media/photo1.jpg')
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id = chat_id, photo=photo_file_id, caption='опис', reply_markup=ikb_menu)


@dp.message_handler(text = '/album')
async def send_album(message: Message):

    photo_file_id = 'AgACAgIAAxkBAAIFFmMWPNXiZ1nGbdA8fe1VfPVmfVCoAAKMxDEb1lS4SPGrpPRmMkBBAQADAgADeQADKQQ'
    photo_bytes = InputFile(path_or_bytesio='media/photo1.jpg')
    video_file_id = 'BAACAgIAAxkBAAIFMGMWQSNuSqZ8KOA_22HUwc7YSbPpAAKyHAAC1lS4SFmYT-XcmQ1SKQQ'

    album = MediaGroup()
    album.attach_photo(photo = photo_file_id)
    album.attach_photo(photo = photo_file_id)
    album.attach_video(video = video_file_id, caption= 'Опис')

    await message.answer_media_group(media=album)