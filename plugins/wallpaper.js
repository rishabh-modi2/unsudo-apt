const { MessageType } = require('@adiwajshing/baileys')
const fetch = require('node-fetch')

let handler = async (m, { conn }) => {
    try {
      await m.reply(global.wait)
        let res = await fetch(global.API('xteam', '/randomimage/wpmobile', {}, 'APIKEY'))
        let img = await res.buffer()
        conn.sendMessage(m.chat, img, MessageType.image, {
            quoted: m, caption: '*©Rishabh-bot*'
        })
    } catch (e) {
        console.log(e)
        throw '_*Owner belum membayar tagihan bar ini*_'
    }
}
//handler.help = ['wallpaper','wp']
//handler.tags = ['weebs']
handler.command = /^(wallpaper|wp)$/i
handler.premium = false


module.exports = handler