from goal_based_agent import goal_based_agent


def run_agent_loop():
    print("Goal-based temperature agent (goal: 72°F)")
    while True:
        temperature_input = input("Enter current temperature in °F (or 'q' to quit): ").strip()
        if temperature_input.lower() in {"q", "quit", "exit"}:
            print("Agent stopped.")
            break

        try:
            temperature = float(temperature_input)
        except ValueError:
            print("Please enter a number or 'q' to quit.")
            continue

        action = goal_based_agent(temperature)
        print(f"Temperature: {temperature:g}°F | Goal: 72°F | Action: {action}")


if __name__ == "__main__":
    run_agent_loop()