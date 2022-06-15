import discord
import asyncio
from discord.ext import commands
from discord.ui import View
from Version import code_version


class HelpSelectView(View):
    def __init__(self, ctx):
        super().__init__(timeout=60)
        self.ctx = ctx

    @discord.ui.select(
            min_values=1,
            max_values=1,
            placeholder="Select a category...",
            options=[
                discord.SelectOption(label="General", description="General help..."),
                discord.SelectOption(label="Moderation", description="Moderation command help..."),
                discord.SelectOption(label="Anniversaries", description="Anniversary command help..."),
                discord.SelectOption(label="Music", description="Music command help..."),
                discord.SelectOption(label="Fun", description="Fun command help..."),
                discord.SelectOption(label="Tournaments/Betting", description="Tour command help..."),
                discord.SelectOption(label="Misc", description="Misc command help...")
            ])
    async def callback(self, select, interaction):
        if select.values[0] == "General":
            embed = discord.Embed(
            colour= discord.Colour.orange()
            )
            embed.set_author(name="All of these are slash commands, and thank you, for using my bot.")
            embed.add_field(name="***Formatting***", value="Commands in <> are work in progress. Commands in 'apostrophes' require special role to execute, and the role's name is in brackets next to the section..", inline=False)
            embed.add_field(name="***Moderation***", value="`Clear`  `Kick`  `Ban`  `Unban`  `Banlist` `Blacklist` `BlacklistAdd` `BlacklistRm`", inline=False)
            embed.add_field(name="***Fun***", value="`Rick`  `Hyper`  `UwUsify`  `CoinFlip`", inline=False)
            embed.add_field(name="***Custom tournaments/betting*** (Dealer)", value="`<Balance>`  `<Bet>`  `<Donate>` `'<Give>'`  `'<CreateBet>'`", inline=False)
            embed.add_field(name="***Misc***", value="`Ping`  `Colors`  `BotBug`  `BotSuggest`", inline=False)
            embed.set_footer(text=f"Code version - {code_version}")
            await interaction.response.edit_message(embed=embed)
    
        if select.values[0] == "Moderation":
            embed = discord.Embed(
            colour= discord.Colour.brand_red()
            )
            embed.set_author(name="These are moderation commands and their usage.")
            embed.add_field(name="***Formatting***", value="Commands in <> are work in progress.", inline=False)
            embed.add_field(name="***Clear***", value="`Clears the specified amount of messages. Usage: /clear $amount$`", inline=False)
            embed.add_field(name="***Kick***", value="`Kicks the mentioned member off of the server. Usage: /kick $@member$ $reason$`", inline=False)
            embed.add_field(name="***Ban***", value="`Bans the mentioned member. Usage: /ban $@member$ $reason$`", inline=False)
            embed.add_field(name="***Unban***", value="`Unbans the specified member. Usage: /ban $username#discriminator$`", inline=False)
            embed.add_field(name="***Banlist***", value="`Prints out specified amount of bans from the server. Usage: /banlist $amount$`", inline=False)
            embed.add_field(name="***Blacklist***", value="`Prints out the servers frase blacklist. Usage: /blacklist`", inline=False)
            embed.add_field(name="***BlacklistAdd***", value="`Adds a frase to the servers blacklist. Usage: /blacklistadd $frase$`", inline=False)
            embed.add_field(name="***BlacklistRm***", value="`Removes a frase from the servers blacklist. Usage: /blacklistrm $frase$`", inline=False)
            embed.set_footer(text=f"Code version - {code_version}")
            await interaction.response.edit_message(embed=embed)

        if select.values[0] == "Anniversaries":
            embed = discord.Embed(
             colour= discord.Colour.fuchsia()
            )
            embed.set_author(name="These are Anniversary commands and their usage.")
            embed.add_field(name="***Formatting***", value="Commands in <> are work in progress.", inline=False)
            embed.add_field(name="***Important***", value="For the anniversaries to work the server needs a text channel with the exact name(copy-paste): `🧁anniversaries🧁`, and permissions to send messages there!", inline=False)
            embed.add_field(name="***AddBday***", value="`Lets you add your birthday to this servers database! Usage: /addbday $day$ $month$ $age$`", inline=False)
            embed.add_field(name="***AddNday***", value="`Lets you add your nameday to this servers database! Usage: /addnday $day$ $month$ $name$`", inline=False)
            embed.add_field(name="***RmBday***", value="`Let's you remove your birthday from this servers database if you so wish. Usage: /rmbday`", inline=False)
            embed.add_field(name="***RmNday***", value="`Let's you remove your nameday from this servers database if you so wish. Usage: /rmnday`", inline=False)
            embed.set_footer(text=f"Code version - {code_version}")
            await interaction.response.edit_message(embed=embed)

        if select.values[0] == "Fun":
            embed = discord.Embed(
            colour= discord.Colour.nitro_pink()
            )
            embed.set_author(name="These are fun commands and their usage.")
            embed.add_field(name="***Formatting***", value="Commands in <> are work in progress.", inline=False)
            embed.add_field(name="***Rick***", value="`Never gonna give you up! Never gonna let you down! Usage: /rick`", inline=False)
            embed.add_field(name="***Hyper***", value="`Links an URL in an embeded text (creates a hyperlink). Usage: /hyper $Title$ $URL$`", inline=False)
            embed.add_field(name="***UwUsify***", value="`UwU-sifies the inputted text. Usage: /uwusify $Text$`", inline=False)
            embed.add_field(name="***CoinFlip***", value="`Flips a coin. Usage: /coinflip`", inline=False)
            embed.add_field(name="***Insult***", value="`Insults the mentioned member. Usage: /insult $@member$`", inline=False)
            embed.add_field(name="***AddInsult***", value="`Adds your own insult to the list. Usage: /addinsult $Insult$`", inline=False)
            embed.set_footer(text=f"Code version - {code_version}")
            await interaction.response.edit_message(embed=embed)

        if select.values[0] == "Tournaments/Betting":
            embed = discord.Embed(
            colour= discord.Colour.dark_teal()
            )
            embed.set_author(name="These are betting commands and their usage.")
            embed.add_field(name="***Formatting***", value="Commands in <> are work in progress. Commands in 'apostrophes' require special role to execute (Dealer, CEODealer).", inline=False)
            embed.add_field(name="***Register***", value="`Opens an account for you in the current server. Usage: /register`", inline=False)
            embed.add_field(name="***Balance***", value="`Displays betting balance only from this server. Usage: /balance`", inline=False)
            embed.add_field(name="***Bet***", value="`Lets you bet on an ongoing tournament/bet. Usage: /bet $id$ $amount$`", inline=False)
            embed.add_field(name="***Give***", value="`Lets you to give your money to someone else. Usage: /give $@member$ $amount$`", inline=False)
            embed.add_field(name="***'Donate'***", value="`Lets the dealer/-s to donate balance to a member. Usage: /donate $@member$ $amount$`", inline=False)
            embed.add_field(name="***'CreateBet'***", value="`Lets the dealer/-s to create a bet. Usage: /createbet ---coming---soon---`", inline=False)
            embed.add_field(name="***'ResetBal'***", value="`Lets the CEOdealer/-s to reset balance of a member. Usage: /resetbal $@member$ $amount$`", inline=False)
            embed.add_field(name="***'ResetServerBal'***", value="`Lets the CEOdealer/-s to reset balance of everyone in the server. Usage: /resetserverbal $amount$`", inline=False)
            embed.set_footer(text=f"Code version - {code_version}")
            await interaction.response.edit_message(embed=embed)

        if select.values[0] == "Misc":
            embed = discord.Embed(
             colour= discord.Colour.fuchsia()
            )
            embed.set_author(name="These are miscellaneous commands and their usage.")
            embed.add_field(name="***Formatting***", value="Commands in <> are work in progress.", inline=False)
            embed.add_field(name="***Ping***", value="`Checks the bots ping. Usage: /ping`", inline=False)
            embed.add_field(name="***Colors***", value="`Sends an embed with the selected color. /colors $color$`", inline=False)
            embed.add_field(name="***BotBug***", value="`Report a bug to me! Usage: /botbug $Title$ $Bug$`", inline=False)
            embed.add_field(name="***BotSuggest***", value="`Suggest a feature! Usage: /botsuggest $Title$ $Suggestion$`", inline=False)
            embed.set_footer(text=f"Code version - {code_version}")
            await interaction.response.edit_message(embed=embed)
        

    async def on_timeout(self):
        self.clear_items 


class CreateBetModal(discord.ui.Modal):
    def __init__(self) -> None:
        super().__init__("Create Bet")
        
        self.add_item(discord.ui.InputText(label="Who this bet is about?", placeholder="The matchpoint between Jhonny and Pilgrim?", style=discord.InputTextStyle.short))
        self.add_item(
            discord.ui.InputText(
                label="Description",
                placeholder="The fight of the century right?",
                style=discord.InputTextStyle.long,
                max_length=256
            )
        )
        self.add_item(
            discord.ui.InputText(
                label="The bet-ons",
                placeholder="Who to bet on? One per line. Two MAX rn",
                style=discord.InputTextStyle.long,
                max_length=100
            )
        )
        self.add_item(
            discord.ui.InputText(
                label="Minutes to have the bets open",
                placeholder="Enter 0 if you wish to close ir manually.",
                min_length=1,
                max_length=8
            )
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Building bet")
        await interaction.delete_original_message()
        self.stop()
