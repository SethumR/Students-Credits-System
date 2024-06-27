from graphics import*
from datetime import*

def main():
    outcomes = []
    list1 = []
    progress_count = 0
    trailer_count = 0
    exclude_count = 0
    retriever_count = 0

    while True:
        input1 = input("Enter you are (student/staff): ") 
        if input1 not in ["student","staff"]:
            print("Invalid Input")
            continue
        else:
            break
        
    
    while True:
            while True: 
                try:  
                    pass_credits = int(input("Enter your credits at pass: "))
                    if pass_credits not in [0, 20, 40, 60, 80, 100, 120]:
                        print("Out of range")
                        continue
                    else:
                        break 
                except ValueError:
                    print("Integer required")

            while True:
                try: 
                    defer_credits = int(input("Enter your credits at defer: "))
                    if defer_credits not in [0, 20, 40, 60, 80, 100, 120]:
                        print("Out of range")
                        continue
                    else:
                        break
                except ValueError:
                    print("Integer required")
                    
            while True:
                try:
                    fail_credits = int(input("Enter your credits at fail: "))
                    if fail_credits not in [0, 20, 40, 60, 80, 100, 120]:
                        print("Out of range")
                        continue
                    else:
                        break
                except ValueError:
                    print("Integer required")

            total_credits = pass_credits + defer_credits + fail_credits

            if total_credits == 120:
                if pass_credits == 120:
                    outcome = "Progress"
                    progress_count += 1
                elif pass_credits == 100:
                    outcome = "Module trailer" 
                    trailer_count += 1
                elif fail_credits >= 80: 
                    outcome = "Exclude"
                    exclude_count += 1
                else:
                    outcome = "Module retriever"
                    retriever_count += 1
            else:
                outcome = "Total incorrect"
            print(outcome)
            if input1 == "staff": 
                outcomes.append(outcome)
                if outcome != "Total incorrect":
                    outcome = (outcome + "-" + str(pass_credits) + "," + str(defer_credits) + "," + str(fail_credits))
                    list1.append(outcome)
        
                final = input("Would you like to enter another set of data? (y/q) ?")
                if final == "y":
                    continue
                elif final == "q":
                    break


            else:
                break
    if input1 == "staff":
        now = datetime.now()
        textfile= now.strftime("%Y_%m_%d_%H_%M.txt")       
        with open(textfile, "a") as file:
            for data in list1:
                print(data)
                file.write(data + "\n")
        total_outcomes = progress_count + trailer_count + exclude_count + retriever_count

        win = GraphWin("Progression Outcomes Histogram", 700, 600)
        # Calculate the number of students in each category
        progress_count = outcomes.count("Progress")
        trailer_count = outcomes.count("Module trailer")
        retriever_count = outcomes.count("Module retriever")
        exclude_count = outcomes.count("Exclude")

        # Draw the histogram bars
        bar_width = 70
        bar_height = 220

        progress_bar = Rectangle(Point(50, 350), Point(50 + bar_width, 350 - (progress_count * bar_height / len(outcomes))))
        progress_bar.setFill("Light Green")
        progress_bar.draw(win)

        trailer_bar = Rectangle(Point(150, 350), Point(150 + bar_width, 350 - (trailer_count * bar_height / len(outcomes))))
        trailer_bar.setFill("Orange")
        trailer_bar.draw(win)

        retriever_bar = Rectangle(Point(250, 350), Point(250 + bar_width, 350 - (retriever_count * bar_height / len(outcomes))))
        retriever_bar.setFill("Green")
        retriever_bar.draw(win)

        exclude_bar = Rectangle(Point(350, 350), Point(350 + bar_width, 350 - (exclude_count * bar_height / len(outcomes))))
        exclude_bar.setFill("yellow")
        exclude_bar.draw(win)

        # Display the outcome 
        outcome_text = f"Histogram Results"
        outcome_label = Text(Point(250,60), outcome_text)
        outcome_label.draw(win)           

        outcome_text = f" Progress  " 
        outcome_label = Text(Point(90, 370), outcome_text) 
        outcome_label.draw(win)

        outcome_text = f" Trailer  "
        outcome_label = Text(Point(189, 370), outcome_text)
        outcome_label.draw(win)

        outcome_text = f" Retriever  "
        outcome_label = Text(Point(288, 370), outcome_text)
        outcome_label.draw(win)

        outcome_text = f" Excluded   " 
        outcome_label = Text(Point(392, 370), outcome_text)
        outcome_label.draw(win)

        outcome_text = f"{total_outcomes} Outcomes in Total  "
        outcome_label = Text(Point(130, 400), outcome_text) 
        outcome_label.draw(win)

        # Create count Label
        count_text = f"{progress_count}"
        count_label = Text(Point(50 + bar_width / 2, 340 - (progress_count * bar_height / len(outcomes))), count_text)
        count_label.draw(win)

        count_text = f"{trailer_count}"
        count_label = Text(Point(150 + bar_width / 2, 340 - (trailer_count * bar_height / len(outcomes))), count_text)
        count_label.draw(win)

        count_text = f"{retriever_count}"
        count_label = Text(Point(250 + bar_width / 2, 340 - (retriever_count * bar_height / len(outcomes))), count_text)
        count_label.draw(win)

        count_text = f"{exclude_count}"
        count_label = Text(Point(350 + bar_width / 2, 340 - (exclude_count * bar_height / len(outcomes))), count_text)
        count_label.draw(win)

        # Wait for the user to close the window
        win.getMouse()
        win.close() 


if __name__ == "__main__":
        main()
