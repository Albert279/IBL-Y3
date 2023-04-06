"""
The function asks the user for the answer to the Great Question of Life, the Universe, and
Everything and checks if the answer is "42", "forty-two", or "forty two".
"""
def main():

    answer = input("What's the Answer to the Great Question of Life, the Universe, and Everything? ")
    if great_question(answer) == True:
        print("Yes.")
    else:
        print("No.")
        
def great_question(answer):
    return answer == "42" or answer == "forty-two" or answer == "forty two"

main()