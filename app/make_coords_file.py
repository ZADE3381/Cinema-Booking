currentLetter = "A"
currentNumber = 4
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
while currentLetter != "U":
    currentNumberString = str(currentNumber)
    print(
f"""
if string == "{currentLetter}1":
    return [{currentNumberString}, 2]
if string == "{currentLetter}2":
    return [{currentNumberString}, 3]
if string == "{currentLetter}3":
    return [{currentNumberString}, 4]
if string == "{currentLetter}4":
    return [{currentNumberString}, 5]
if string == "{currentLetter}5":
    return [{currentNumberString}, 6]
if string == "{currentLetter}6":
    return [{currentNumberString}, 7]
if string == "{currentLetter}7":
    return [{currentNumberString}, 8]
if string == "{currentLetter}8":
    return [{currentNumberString}, 9]
if string == "{currentLetter}9":
    return [{currentNumberString}, 10]
if string == "{currentLetter}10":
    return [{currentNumberString}, 11]
if string == "{currentLetter}11":
    return [{currentNumberString}, 14]
if string == "{currentLetter}12":
    return [{currentNumberString}, 15]
if string == "{currentLetter}13":
    return [{currentNumberString}, 16]
if string == "{currentLetter}14":
    return [{currentNumberString}, 17]
if string == "{currentLetter}15":
    return [{currentNumberString}, 18]
if string == "{currentLetter}16":
    return [{currentNumberString}, 19]
if string == "{currentLetter}17":
    return [{currentNumberString}, 20]
if string == "{currentLetter}18":
    return [{currentNumberString}, 21]
if string == "{currentLetter}19":
    return [{currentNumberString}, 22]
if string == "{currentLetter}20":
    return [{currentNumberString}, 23]
""")
    currentNumber = currentNumber + 1
    currentLetter = alphabet[currentNumber - 4]
# currentLetter = "A"
# currentNumber = 4
# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
# while currentLetter != "U":
#     currentNumberString = str(currentNumber)
#     print(
# f"""
# if array == [{currentNumberString}, 2]:
#     return "{currentLetter}1"
# if array == [{currentNumberString}, 3]:
#     return "{currentLetter}2"
# if array == [{currentNumberString}, 4]:
#     return "{currentLetter}3"
# if array == [{currentNumberString}, 5]:
#     return "{currentLetter}4"
# if array == [{currentNumberString}, 6]:
#     return "{currentLetter}5"
# if array == [{currentNumberString}, 7]:
#     return "{currentLetter}6"
# if array == [{currentNumberString}, 8]:
#     return "{currentLetter}7"
# if array == [{currentNumberString}, 9]:
#     return "{currentLetter}8"
# if array == [{currentNumberString}, 10]:
#     return "{currentLetter}9"
# if array == [{currentNumberString}, 11]:
#     return "{currentLetter}10"
# if array == [{currentNumberString}, 14]:
#     return "{currentLetter}11"
# if array == [{currentNumberString}, 15]:
#     return "{currentLetter}12"
# if array == [{currentNumberString}, 16]:
#     return "{currentLetter}13"
# if array == [{currentNumberString}, 17]:
#     return "{currentLetter}14"
# if array == [{currentNumberString}, 18]:
#     return "{currentLetter}15"
# if array == [{currentNumberString}, 19]:
#     return "{currentLetter}16"
# if array == [{currentNumberString}, 20]:
#     return "{currentLetter}17"
# if array == [{currentNumberString}, 21]:
#     return "{currentLetter}18"
# if array == [{currentNumberString}, 22]:
#     return "{currentLetter}19"
# if array == [{currentNumberString}, 23]:
#     return "{currentLetter}20"
# """)
#     currentNumber = currentNumber + 1
#     currentLetter = alphabet[currentNumber - 4]
# currLetter = "A"
# count = 0
# while currLetter != "U":
#     print(
#         f"""
#             <tr>
#                 <td><div class="seat">{currLetter}1</div> </td>
#                 <td><div class="seat">{currLetter}2</div></td>
#                 <td><div class="seat">{currLetter}3</div></td>
#                 <td><div class="seat">{currLetter}4</div></td>
#                 <td><div class="seat">{currLetter}5</div></td>
#                 <td><div class="seat">{currLetter}6</div> </td>
#                 <td><div class="seat">{currLetter}7</div></td>
#                 <td><div class="seat">{currLetter}8</div></td>
#                 <td><div class="seat">{currLetter}9</div></td>
#                 <td><div class="seat">{currLetter}10</div></td>
#                 <td class="walk">    </td>
#                 <td class="walk">    </td>
#                 <td><div class="seat">{currLetter}11</div> </td>
#                 <td><div class="seat">{currLetter}12</div></td>
#                 <td><div class="seat">{currLetter}13</div></td>
#                 <td><div class="seat">{currLetter}14</div></td>
#                 <td><div class="seat">{currLetter}15</div> </td>
#                 <td><div class="seat">{currLetter}16</div></td>
#                 <td><div class="seat">{currLetter}17</div></td>
#                 <td><div class="seat">{currLetter}18</div></td>
#                 <td><div class="seat">{currLetter}19</div></td>
#                 <td><div class="seat">{currLetter}20</div></td>
#             </tr>
# """)
#     count += 1
#     currLetter = alphabet[count]
