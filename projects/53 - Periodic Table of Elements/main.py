import csv
import sys
import re
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_elements():
    elements_file = open('periodictable.csv', encoding='utf-8')
    elements_csv_reader = csv.reader(elements_file)
    elements_data = list(elements_csv_reader)
    elements_file.close()
    
    elements = {}
    
    for line in elements_data:
        if not line or len(line) < 13:
            continue
            
        element = {
            'Atomic Number': line[0],
            'Symbol': line[1],
            'Element': line[2],
            'Origin of name': line[3],
            'Group': line[4],
            'Period': line[5],
            'Atomic weight': line[6] + ' u',
            'Density': line[7] + ' g/cm³',
            'Melting point': line[8] + ' K',
            'Boiling point': line[9] + ' K',
            'Specific heat capacity': line[10] + ' J/(g*K)',
            'Electronegativity': line[11],
            'Abundance in earth\'s crust': line[12] + ' mg/kg'
        }
        
        for key, value in element.items():
            element[key] = re.sub(r'\[(I|V|X)+\]', '', value)
            element[key] = element[key].replace('[X]', '').replace('[III]', '').replace('[IV]', '')
            element[key] = element[key].replace('[V]', '').replace('[VI]', '').replace('[VII]', '')
            element[key] = element[key].replace('[VIII]', '').replace('[IX]', '').replace('[XI]', '')
            element[key] = element[key].replace('[XII]', '').replace('[XIII]', '').replace('[XIV]', '')
            element[key] = element[key].replace('[XV]', '').replace('(2)', '').replace('(3)', '')
            element[key] = element[key].replace('(4)', '').replace('(5)', '').replace('(6)', '')
            element[key] = element[key].replace('(7)', '').replace('(8)', '').replace('(9)', '')
            element[key] = element[key].replace('(10)', '').strip()
        
        elements[line[0]] = element
        elements[line[1]] = element
        elements[line[2].lower()] = element
    
    return elements

def display_periodic_table():
    print("\n" + "="*80)
    print("                      🧪 PERIODIC TABLE OF ELEMENTS 🧪")
    print("="*80)
    print("""
      1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
    1 H                                                  He
    2 Li Be                               B  C  N  O  F  Ne
    3 Na Mg                               Al Si P  S  Cl Ar
    4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
    5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
    6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
    7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

    Lanthanides:  Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
    Actinides:    Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr
    """)
    print("="*80)

def display_element_info(element_data, search_term):
    print("\n" + "🔬 " + "="*78 + " 🔬")
    print(f"   ELEMENT INFO: {element_data['Element'].upper()} ({element_data['Symbol']})")
    print("="*80)
    
    properties = [
        ('Atomic Number', '⚛️'),
        ('Symbol', '🔤'),
        ('Element', '📛'),
        ('Origin of name', '📚'),
        ('Group', '📊'),
        ('Period', '📈'),
        ('Atomic weight', '⚖️'),
        ('Density', '🧱'),
        ('Melting point', '🌡️'),
        ('Boiling point', '💨'),
        ('Specific heat capacity', '🔥'),
        ('Electronegativity', '⚡'),
        ('Abundance in earth\'s crust', '🌍')
    ]
    
    for prop, icon in properties:
        value = element_data[prop]
        if value and value != '–' and value != ' u' and value != ' g/cm³':
            print(f"{icon} {prop:.<30} {value}")
    
    print("="*80)

def get_element_suggestions(search_term, elements):
    suggestions = []
    search_lower = search_term.lower()
    
    for key, element in elements.items():
        if (search_lower in element['Element'].lower() or 
            search_lower in element['Symbol'].lower() or
            search_lower == key.lower()):
            if element not in suggestions:
                suggestions.append(element)
    
    return suggestions[:5]

def search_by_property(elements):
    print("\n🔍 Search by property:")
    print("1. Atomic Number Range")
    print("2. Group")
    print("3. Period")
    print("4. State at Room Temperature")
    
    choice = input("Enter choice (1-4): ").strip()
    
    if choice == '1':
        try:
            start = int(input("Start atomic number: "))
            end = int(input("End atomic number: "))
            results = []
            for key, element in elements.items():
                try:
                    atomic_num = int(element['Atomic Number'])
                    if start <= atomic_num <= end and element not in results:
                        results.append(element)
                except:
                    pass
            return sorted(results, key=lambda x: int(x['Atomic Number']))[:10]
        except:
            return []
    
    elif choice == '2':
        group = input("Enter group number: ").strip()
        results = []
        for key, element in elements.items():
            if element['Group'] == group and element not in results:
                results.append(element)
        return results[:10]
    
    elif choice == '3':
        period = input("Enter period number: ").strip()
        results = []
        for key, element in elements.items():
            if element['Period'] == period and element not in results:
                results.append(element)
        return results[:10]
    
    elif choice == '4':
        print("States: gas, liquid, solid")
        state = input("Enter state: ").lower().strip()
        results = []
        for key, element in elements.items():
            melting = element['Melting point'].replace(' K', '').strip()
            boiling = element['Boiling point'].replace(' K', '').strip()
            try:
                if melting and melting != '–' and boiling and boiling != '–':
                    mp = float(melting)
                    bp = float(boiling)
                    room_temp = 298.15
                    
                    if state == 'gas' and bp < room_temp:
                        if element not in results:
                            results.append(element)
                    elif state == 'liquid' and mp < room_temp < bp:
                        if element not in results:
                            results.append(element)
                    elif state == 'solid' and mp > room_temp:
                        if element not in results:
                            results.append(element)
            except:
                pass
        return results[:10]
    
    return []

def main():
    try:
        elements = load_elements()
    except FileNotFoundError:
        print("❌ Error: periodictable.csv not found!")
        print("Please ensure the CSV file is in the workspace root directory.")
        return
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return
    
    while True:
        display_periodic_table()
        print("💡 Commands:")
        print("   • Enter element symbol, name, or atomic number")
        print("   • Type 'search' for advanced property search")
        print("   • Type 'random' for a random element")
        print("   • Type 'quit' to exit")
        print("-" * 80)
        
        response = input("🔍 Enter command: ").strip()
        
        if response.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Thanks for exploring the periodic table!")
            break
        
        elif response.lower() == 'search':
            results = search_by_property(elements)
            if results:
                print(f"\n🎯 Found {len(results)} elements:")
                for i, element in enumerate(results, 1):
                    print(f"{i}. {element['Element']} ({element['Symbol']}) - Atomic Number: {element['Atomic Number']}")
                
                try:
                    choice = int(input("\nSelect element number for details: ")) - 1
                    if 0 <= choice < len(results):
                        clear_screen()
                        display_element_info(results[choice], response)
                        input("\n📖 Press Enter to continue...")
                except:
                    print("Invalid selection.")
            else:
                print("❌ No elements found matching criteria.")
                input("Press Enter to continue...")
        
        elif response.lower() == 'random':
            import random
            atomic_numbers = [str(i) for i in range(1, 119)]
            random_element = elements[random.choice(atomic_numbers)]
            clear_screen()
            display_element_info(random_element, response)
            input("\n📖 Press Enter to continue...")
        
        elif response:
            if response in elements:
                clear_screen()
                display_element_info(elements[response], response)
                input("\n📖 Press Enter to continue...")
            else:
                suggestions = get_element_suggestions(response, elements)
                if suggestions:
                    print(f"\n❓ '{response}' not found. Did you mean:")
                    for i, suggestion in enumerate(suggestions, 1):
                        print(f"{i}. {suggestion['Element']} ({suggestion['Symbol']})")
                    
                    try:
                        choice = int(input("\nSelect element number (0 to cancel): "))
                        if 1 <= choice <= len(suggestions):
                            clear_screen()
                            display_element_info(suggestions[choice-1], response)
                            input("\n📖 Press Enter to continue...")
                    except:
                        pass
                else:
                    print(f"❌ '{response}' not found. Please try again.")
                    input("Press Enter to continue...")
        
        clear_screen()

if __name__ == '__main__':
    main()