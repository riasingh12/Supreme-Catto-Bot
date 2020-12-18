require("dotenv").config();
const Discord = require('discord.js');
const { prefix, token } = require('./config.json');
const client = new Discord.Client(); // js object that connects to discord api to manage to run the bot


client.login(token);


client.on('ready', readyDiscord);

function readyDiscord() {
  console.log("We're online bishes");
}

const replies = [
  'chutiya',
  'lawda lassan',
  'allahuakbar',
  'bhadwe',
  'motherboard',
  'nigga',
  'abey saale'
]

client.on('message', message => {
	if (!message.content.startsWith(prefix) || message.author.bot) return; // dont reply to bots or if prefix false

	const args = message.content.slice(prefix.length).trim().split(/ +/);
  const command = args.shift().toLowerCase();
  
  if (message.content === `server`) {
    message.channel.send(`Server name: ${message.guild.name}\nTotal members: ${message.guild.memberCount}`);
  }
  else if (message.content === `user-info`) {
    message.channel.send(`Your username: ${message.author.username}\nYour ID: ${message.author.id}`);
  }
  else if (message.content === startsWith(`ping`)) {
    message.channel.send('Boop.');
  }
  else if (msg.content === startsWith(`ping`)) {
    msg.channel.send("Kya hai bey, padhai likhai karo");
  }
  else if (msg.content === startsWith(`Shame me senpai`)) {
    const index = Math.floor(Math.random() * replies.length);
    msg.channel.send(replies[index]);
  }
}










