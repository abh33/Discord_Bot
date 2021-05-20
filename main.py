import os
import random
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
from dotenv import load_dotenv

def get_village(village, n):
	for ville in village.keys():
		if n in village[ville]:
			return ville

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

village = {"W-ville" : [1, 2, 3, 4, 5, 6, 7, 41, 25], "E-ville" : [10, 11, 12, 14, 13, 15, 38, 39, 33], "M-ville" : [16, 17, 18, 19, 20, 8, 9, 24],	"R-ville" : [27, 28, 30, 31, 21, 22, 23, 36]}

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')
	
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    # print(message.channel.name, type(message.channel.name))
    if message.content == 'test' and message.channel.name == '🕵-verification-room':
        await message.channel.send('testing 1 2 3!')

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="🕵-verification-room")
    await channel.send('Hi ' + member.name+ ' , welcome to eYSIP-2021 Discord server! Kindly refer this sheet : https://docs.google.com/spreadsheets/d/1uUSt9RwidrUZxJhlCCgZo0gpK5JHiHf4T9FUDeh514g/edit?usp=sharing for your assigned project\'s ID.\nPlease use the command "$intern <Project ID>" in this channel for the appropriate role ville role to be assigned to you. \nExample: \n> $intern 1')

@bot.command(name='intern', help='Assigns Project Channel', pass_context=True)
# @commands.has_role("Admin")
async def intern_pid(ctx, pid_number:int):
#     project_roles = {1 : '1 - eYLAD: e-Yantra Learning Analytics Dashboard',2 : '2 - Designing affordances for collaborative learning on MOOC portal',3 : '3 - AutoQuery',4 : '4 - CloudSim',\
#      5 : '5 - Testing and Verification of Hardware Theme Codes',6 : '6 - Gradefast++',7 : '7 - eYRC AutoGrader ',41 : '41 - Map enabled Disaster Relief and Response Platform',\
#      10 : '10 - Model Based Design approach for Embedded Systems',11 : '11 - Hardware Software Co-Design Approach for developing Embedded Systems Application',\
#      12 : '12 - Implementation of AI/ML  and DSP libraries using AJIT vector instructions.',14 : '14 - IoT project implementation using functional languages',\
#      13 : '13 - Interfacing a Xilinx Ethernet MAC to the AJIT processor core.',15 : '15 - Machine Learning on FPGA',38 : '38 - Precision landing of hybrid UAVs on a moving platform',\
#      39 : '39 - Arrestor and battery swapping mechanism for hybrid UAVs',16 : '16 - Steps towards building a MIPS Processor on FPGA',17 : '17 - IoT Applications in Simulated environments',\
#      18 : '18 - Designing and Developing Robotics Projects using ROS1',19 : '19 - Designing and Developing Robotics Projects using ROS2',\
#      20 : '20 - Robot Simulations - Exploring the inner- workings of CoppeliaSim',36 : '36 - Augmented Reality Manipulator',33 : '33 - e-Yantra Trophy',8 : '8 - Music Genre Classification',\
#      9 : '9 - Audio Mixing using Python (Classical and Western fusion)',24 : '24 - Chatbot',25 : '25 - Verif-ID',27 : '27 - Simulation dynamics of a Quadruped in ROS-Gazebo',\
#      28 : '28 - Model-based designing of a two-legged-wheeled robot with ROS and Gazebo',30 : '30 - Package Delivery using Blockchain and ROS',31 : '31 - Robot-Soccer',\
#      21 : '21 - 3D perception',22 : '22 - Outdoor Navigation(present estimation)',23 : '23 - Perception for agricultural environments'}


    
    member = ctx.message.author
    role = discord.utils.get(member.guild.roles, name='🧝‍♂️ intern')
    await member.add_roles(role)
    project_roles = ["W-ville", "R-ville", "E-ville", "M-ville"]
    flag = False
    for project_role in project_roles:
        role_discord = discord.utils.find(lambda r: r.name == project_role, ctx.message.guild.roles)
        if role_discord in member.roles:
            flag = True

    if flag == False:
        # print(get_village(village, pid_number))
        project_role = discord.utils.get(member.guild.roles, name=get_village(village, pid_number))
        # print()
        await member.add_roles(project_role)
        await ctx.send("Hi " + member.name + "! You have been assigned the following role(s): intern, " + project_role.name)
    else:
        await ctx.send("Hi " + member.name + "! You have already been assigned a ville!!")
		
bot.run(TOKEN)