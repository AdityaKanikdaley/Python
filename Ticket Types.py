ticket_code=input("\n\nEnter your ticket code: ")
ticket_type="Invalid Code !"    #defalut type
if(ticket_code=='E' or ticket_code=='e'):
    ticket_type="Early Bird ticket !"
elif(ticket_code=='D' or ticket_code=='d'):
    ticket_type="Discount ticket !"
elif(ticket_code=='V' or ticket_code=='v'):
    ticket_type="VIP ticket !"
elif(ticket_code=='S' or ticket_code=='s'):
    ticket_type="Standard ticket !"
elif(ticket_code=='C' or ticket_code=='c'):
    ticket_type="Child ticket !"
print("Your ticket type is: ",ticket_type, "\n\n")


