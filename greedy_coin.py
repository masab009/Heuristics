import click

def greedy_coin(change):
    """ 
     so we have pakistani coins available of 
      1rs, 2rs and 5 rs, 10rs and lets say we were building a software for a vending machine
        """
    print(f"Your change for {change} is: ")
    coins_dict = {}
    coins = [10,5,2,1]
    coins_lookup = {10:"10RS Coin",5:"5RS coin",2:"2RS coin",1:"1RS coin"}
    for coin in coins:
        coins_dict[coin] = 0
    
    for coin,value in coins_lookup.items():

        while coin <= change:
            coins_dict[coin] += 1
            change -= coin

    print("Following is the distributions of the coin that you are going to get in change ")

    for coin in coins:
        if coins_dict[coin] >= 0:

            print(f"{coin} : {coins_dict[coin]}")

    return coins_lookup

@click.command()
@click.argument("change",type=float)
def main(change):
    greedy_coin(change)

if __name__ == "__main__":
    main()
