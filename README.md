# simple-railway-game

  
**DISCLAIMER: The contributors and I are trying our best to make this game historically accurate. If you see a historical inconsistency, please open an issue.**  

Hello there!

Sorry about this mess of code. My first code to reach over 150 lines! 

This is a monopoly-like game where player builds railroads in order win. It is based in the 1860s. 

## Gameplay
  
This game requires four people. However, an adjustable party size is in the works.

### Choose between Government funded or privately funded (Factions)

```
Player A: Select how you are going to start your railway: (Government/Private)
```
  
All you need to do is to type the first letter of the organization.
  
**Goverment** gives you less money, but you do not have to pay them back. (and more limitations such as no international lines, but that has not been implemented yet.)
  
**Private** gives you a lot more money, but you have to pay the investors back **with interest**.
  
### Setting up your railway company

#### Government
  
```
Player A, you have chosen to get funded by the Government. You get less money, but you don't have to pay back.
Which project do you want to participate in?
(CA/US)> 
```
  
Currently, there are two countries that you can accept offers from: Canada and the US. Which ever Country you choose, you are limited to that country, with unique challenges (That will be coming soon with Wildcards).  
  
  

#### Private

```
Player C, choose your investor:
Investor A: 7850000.0 3.42% per 6 weeks
Investor B: 9120000.0 2.92% per 2 weeks
Investor C: 13930000.0 2.47% per 4 weeks
>
```
Private companies have to get funded by investors.  
The numbers from left to right are:  
*1. Investment amount*  
*2. Return rate*  
*3. Time when interest applies*  
  
Choose a offering by selecting the investor's letter. Then the investor will pay you that amount of money. But you have to pay them back.  
  
### Select starting city

```
Player A: 
1. Select starting point
2. Random city
> 
```  
It is pretty self explanatory. You can select a starting point, or you can let the program decide it for you. Remember, if your company is government founded, your stations will be limited to that country!
  
### Pay your workers  
