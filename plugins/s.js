const { MessageType } = require('@adiwajshing/baileys')
const { sticker } = require('../lib/sticker')
const uploadFile = require('../lib/uploadFile')
const uploadImage = require('../lib/uploadImage')
let { webp2png } = require('../lib/webp2mp4')
let handler = async (m, { conn, args, usedPrefix, command }) => {
await m.reply(global.wait)
  let stiker = false
  try {
    let q = m.quoted ? m.quoted : m
    let mime = (q.msg || q).mimetype || ''
    if (/webp|image|video/g.test(mime)) {
      if (/video/g.test(mime)) if ((q.msg || q).seconds > 11) return m.reply('Maksimal 10 detik!')
      let img = await q.download()
      if (!img) throw `balas gambar/video/stiker toh de perintah ${usedPrefix + command}`
      let out
      try {
        if (/webp/g.test(mime)) out = await webp2png(img)
        else if (/image/g.test(mime)) out = await uploadImage(img)
        else if (/video/g.test(mime)) out = await uploadFile(img)
        stiker = await sticker(false, out, '© 百鬼あやめ', '© 赤井はあと')
      } catch (e) {
        console.error(e)
        stiker = await sticker(img, false, '© 百鬼あやめ', '© 赤井はあと')
      }
    } else if (args[0]) {
      if (isUrl(args[0])) stiker = await sticker(false, args[0], '© 百鬼あやめ', '© 赤井はあと')
      else return m.reply('URL tidak valid!')
    }
  } catch (e) {
    console.error(e)
    if (Buffer.isBuffer(e)) stiker = e
  } finally {
    if (stiker) await conn.sendMessage(m.chat, stiker, MessageType.sticker, {
      quoted: m
    })
    else throw `Gagal${m.isGroup ? ', balas gambarnya!' : ''}`
  }
}
//handler.help = ['stiker ', 'stiker <url>']
//handler.tags = ['sticker']
handler.command = /^go?$/i
handler.register = true
handler.limit = false

module.exports = handler

const isUrl = (text) => {
  return text.match(new RegExp(/https?:\/\/(www\.)?[-a-zA-Z0-9@:%._+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_+.~#?&/=]*)(jpe?g|gif|png)/, 'gi'))
}
