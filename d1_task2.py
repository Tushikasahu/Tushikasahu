import pandas as pd
repeat = True
ss = []
ff = []
cc = []
pp = []
n  = int(input("Enter the number of bouquets you want to order: "))
while repeat == True:
    # Display the menu
    print("Welcome to the Flower Shop")
    print("Please select an option from the menu below:")
    print("1. Order bouquet and get the price")
    print("2. Display statistics")
    print("3. Exit")
    ch = int(input("Enter your choice (1-3): "))
    if ch == 1:
        size1 = {
        1 : pd.Series(['small',5.5], index=['Type ', 'Mark-Up']),
        2 : pd.Series(['medium',7.5], index=['Type ', 'Mark-Up']),
        3 : pd.Series(['large',9.5], index=['Type ', 'Mark-Up']),
        }
        s = pd.DataFrame(size1)
        print(s)
        flower1 = {
        1 : pd.Series(['rose', 1.2], index=['Type ', 'Mark-Up']),
        2 : pd.Series(['lily', 1.3], index=['Type ', 'Mark-Up']),
        3 : pd.Series(['Carnation', 1.0], index=['Type ', 'Mark-Up']),
        4 : pd.Series(['Daffodil', 1.0], index=['Type ', 'Mark-Up']),
        5 : pd.Series(['Gerbera', 1.1], index=['Type ', 'Mark-Up']),
        6 : pd.Series(['Chrysanthemum', 1.1], index=['Type ', 'Mark-Up']),
        7 : pd.Series(['Assorted', 0.8], index=['Type ', 'Mark-Up']),
        }
        f = pd.DataFrame(flower1)
        print(f)
        color1 = {
        1 : pd.Series(['White', 1.3], index=['Type ', 'Mark-Up']),
        2 : pd.Series(['Red', 1.2], index=['Type ', 'Mark-Up']),
        3 : pd.Series(['Pink', 1.1], index=['Type ', 'Mark-Up']),
        4 : pd.Series(['Yellow', 1.1], index=['Type ', 'Mark-Up']),
        5 : pd.Series(['blue', 1.2], index=['Type ', 'Mark-Up']),
        6 : pd.Series(['Assorted', 1.0], index=['Type ', 'Mark-Up']),
        }
        c = pd.DataFrame(color1)
        print(c)
        sizee = int(input("Enter the size of bouquet (1-3): "))
        ss.append(sizee)
        flowerr = int(input("Enter the flower type (1-7): "))
        ff.append(flowerr)
        colorr = int(input("Enter the color type (1-6): "))
        cc.append(colorr)
        size_type = {1:5.5 , 2: 7.5, 3: 9.5}
        flower_type = {1:1.2, 2:1.3, 3:1.0, 4:1.0, 5:1.1, 6:1.1, 7:0.8}
        color_type = {1:1.3, 2:1.2, 3:1.1, 4:1.1, 5:1.2, 6:1.0}
        size = {1:'Small', 2:'Medium', 3:'Large'}
        flower = {1:'Rose', 2:'Lily', 3:'Carnation', 4:'Daffodil', 5:'Gerbera', 6:'Chrysanthemum', 7:'Assorted'}
        color = {1:'White', 2:'Red', 3:'Pink', 4:'Yellow', 5:'Blue', 6:'Assorted'}
        print(f"Your bouquet size is {size[sizee]}")
        print(f"Your flower type is {flower[flowerr]}")
        print(f"Your color type is {color[colorr]}")
        price = (flower_type[flowerr] + color_type[colorr]) * size_type[sizee]
        pp.append(price)
        print(f"Your total price is {price}")
        print("your bouquet is ordered")
        rp = input("Do you want to order again? (yes/no): ")
        if rp == "no":
            print("""
            ---------------------------------------------------------------------
            |   Sr.no   |    Size     |    Flower    |   Colour    |   Price    |
            ---------------------------------------------------------------------
            """)
            for i in range(n):
                print(f"""
                      | {i+1}  |  {size[ss[i]]}  |  {flower[ff[i]]}  |  {color[cc[i]]}  |  {price}  |
                      -------------------------------------------------------------
                      """)
            repeat = False
    elif ch == 2:
        print("Displaying statistics...")
        s_count = ss.count(1)
        m_count = ss.count(2)
        l_count = ss.count(3)
        r_count = ff.count(1)
        l_count = ff.count(2)
        c_count = ff.count(3)
        d_count = ff.count(4)
        g_count = ff.count(5)
        ch_count = ff.count(6)
        a_count = ff.count(7)
        w_count = cc.count(1)
        r_count = cc.count(2)
        p_count = cc.count(3)
        y_count = cc.count(4)
        b_count = cc.count(5)
        a_count = cc.count(6)
        min_price = min(pp)
        max_price = max(pp)
        range_price = max_price - min_price
        total_bouquets = len(ss)
        total_price = sum(pp)
        average_price = total_price / total_bouquets
        print(f"""
        ---------------------------------------------------------------------
        |Size      | Small     | Medium     | Large      |
        |Freq count|{s_count}  | {m_count}  | {l_count}  |

        |Flower     | Rose       | Lily        | Carnation   | Daffodil    | Gerbera     | Chrysanthemum  | Assorted     |
        |Freq count | {r_count}  | {l_count}   | {c_count}   | {d_count}   | {g_count}   | {ch_count}     | {a_count}    |
 
        |Colour     | White     | Red        | Pink       | Yellow      | Blue       | mixed       |
        |Freq count | {w_count} | {r_count}  | {p_count}  | {y_count}   | {b_count}  | {a_count}    |

        |Statistics | Minimum_price | Maximum_price | Range_of_price | Total_number_of_ordered | Total_bouquets_price | Average_bouquet_price |
        |Values     | {min_price}   | {max_price}   | {range_price}  | {total_bouquets}        | {total_price}        | {average_price}       |
        ---------------------------------------------------------------------
        """)

    elif ch == 3:
        print("Thank you for visiting the Flower Shop!")
        repeat = False
    else:
        print("Invalid choice, please try again.")