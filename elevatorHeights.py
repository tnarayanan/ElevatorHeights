ticks_per_inch = 3.42

base_height = float(input("Elevator base position height (inches): "))
circle_radius = float(input("Circle radius (inches): "))

def getEncoderPos(h):
    return (h + circle_radius - base_height) * ticks_per_inch

def main():
    print()
    print("-----------")
    hatch_rocket_low = float(input("Bottom of LOW rocket hatch (inches): "))
    hatch_rocket_mid = float(input("Bottom of MIDDLE rocket hatch (inches): "))
    hatch_rocket_high = float(input("Bottom of HIGH rocket hatch (inches): "))

    print("-----------")
    hatch_pickup = float(input("Bottom of pickup hatch (inches): "))


    HATCH_PICKUP = getEncoderPos(hatch_pickup) - 22
    HATCH_LOW = getEncoderPos(hatch_rocket_low)
    HATCH_MID = getEncoderPos(hatch_rocket_mid)
    HATCH_HIGH = min(197, getEncoderPos(hatch_rocket_high))

    CARGO_LOW = HATCH_LOW - 20
    CARGO_MID = HATCH_MID - 20
    CARGO_HIGH = 191

    # Results
    print()
    print("   RESULTS   ")
    print("-------------")
    print("HATCH_PICKUP: " + str(HATCH_PICKUP))
    print("HATCH_LOW: " + str(HATCH_LOW))
    print("HATCH_MID: " +  str(HATCH_MID))
    print("HATCH_HIGH: " +  str(HATCH_HIGH))
    print()
    print("CARGO_LOW: " + str(CARGO_LOW))
    print("CARGO_MID: " +  str(CARGO_MID))
    print("CARGO_HIGH: " +  str(CARGO_HIGH))

main()


