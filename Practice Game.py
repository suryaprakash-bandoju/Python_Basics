# List Practice Game

# # Start pack Game
# # --------------------------------------------------------------------------
# dashes = '-' * 100
# pack = []
# print('0, Staring Journey with empty pack.')

# print(pack)
# print(dashes)
# # --------------------------------------------------------------------------

# print('1, Picking Up StarterKit (Armor, Shield, Sword, Potion).')
# pack.append('Armor')
# pack.append('Shield')
# pack.append('Sword')
# pack.append('Potion')

# print(pack)
# print(dashes)

# # Loot a Tresure Chest
# # --------------------------------------------------------------------------

# chest     = ['map', 'gold', 'bow', 'arrows']
# pack += chest

# print('2, Found a chest! Adding contents to pack.')
# print(pack)
# print(dashes)

# # --------------------------------------------------------------------------

# # 3, Visit Merchent
# # --------------------------------------------------------------------------
# print('3, Visiting Merchent to trade items.')
# print('Selling the Shield')
# print(' Upgrading Sword --> Magic Staff')

# pack.remove('Shield')
# ind           = pack.index('Sword')
# pack[ind] = 'Magic Staff'

# print(pack)
# print(dashes)

# # --------------------------------------------------------------------------

# # 4, Check Invertory
# # --------------------------------------------------------------------------
# print('4, Checking pack........')
# print(pack)

# total_items  = len(pack)
# unique_items = len(set(pack))
# potion_count = pack.count('Potion')

# print(f'There are total {total_items} items in the pack.')
# print(f"There are {unique_items} Unique items in the pack.")
# print(f"There are total {potion_count} items in the pack.")
# print(dashes)

# # --------------------------------------------------------------------------

# # 5. Dropped the pack
# # --------------------------------------------------------------------------
# print('5, Dropped the pack! Upside down it goes........')
# pack.reverse()

# print(pack)
# print(dashes)

# # --------------------------------------------------------------------------

# # 6. Sorted the pack
# # --------------------------------------------------------------------------
# print('6. Sorting Items: ')
# pack.sort()

# print(pack)
# print(dashes)
# # --------------------------------------------------------------------------

# # 7. Stolen items during sleep
# # --------------------------------------------------------------------------
# print('7. Stolen items during sleep! oh no!')
# a = pack.pop()
# b = pack.pop(3)
# c = pack.pop()
# stolen = [a, b, c]

# print(f'Stolen items: {stolen}')
# print(pack)
# print(dashes)
# # --------------------------------------------------------------------------

# # Found Magic Ring and Coin Pouch
# # --------------------------------------------------------------------------
# print('8. Found Magic Ring and Coin Pouch adding to pack.')
# ring = 'Magic Ring'
# coin_pouch = ['Gold Coin, Silver Coin']

# pack.insert(0, ring)
# pack.append(coin_pouch)

# print(pack)
# print(dashes)
# # --------------------------------------------------------------------------

# # Half pack disappears
# # --------------------------------------------------------------------------
# print('9. Half pack disappears! What items remain?')

# count = len(pack)
# half = count // 2
# pack = pack[half:]

# print(pack)
# print(dashes)
# # --------------------------------------------------------------------------

# # 10. Bandits attack and steal everything!
# # --------------------------------------------------------------------------
# print('10. Bandits attack and steal everything! pack is now empty.')

# pack = None

# print(pack)
# print(dashes)
# # --------------------------------------------------------------------------

# # End of Game
# print('End of Game. Thanks for playing!')





# Dict Practice
phonebook = {
    'Alice' : '555-1234',
    'Bob'   : '555-5678',
    'Charlie' : '555-8765'
    }
# Add more Items
phonebook['Dave'] = '555-4321'
phonebook['Eve']  = '555-0000'
phonebook['Frank'] = '555-1111'

print(phonebook)

number = phonebook['Alice']
print(f'Calling Alice.... {number}')

number = phonebook['Bob']
print(f'Calling Bob.... {number}')

number = phonebook['Charlie']
print(f'Calling Charlie.... {number}')

number = phonebook['Dave']
print(f'Calling Dave.... {number}')


# Dictionary Advanced Practice

player = {
    'name' : 'surya',
    'level' : 1,
    'health' : 100,
    'class' : 'warrior',
    'backpack' : []
}

# Modify states
player['level'] += 1

# Add items
player['backpack'].append('Health Potion')
player['backpack'].append('Iron Sword')
player['backpack'].append('Wooden Shield')

for i,j in player.items():
    print(f'{i} : {j}')
