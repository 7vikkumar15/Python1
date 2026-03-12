# function definition
def shutdown(status):
    if status == True:
        print("Shutting down")
    elif status == False:
        print("Shutdown aborted")
    else:
        print("Sorry")

# calling the function
shutdown(True)
shutdown(False)
shutdown("yes")