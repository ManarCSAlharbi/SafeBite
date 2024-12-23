# _______________________________________________________________________________________________
# CPCS331: Artificial Intelligence I - 29 October 2024
# Group members: Reema Alghamdi, Rasha Alsabouni, Manar Alharbi, Nora AlGhamdi
# Section: 01 and 02
# _______________________________________________________________________________________________
# 🎉 Welcome to SafeBite! 🎉
# 🍽️ Your Personalized Gluten-Free Nutrition Assistant 🍽️
# 🤖 Utilizing the 'experta' library for intelligent dietary recommendations 🤖
# 🌱 Promoting Healthy Eating Across All Age Groups and Dietary Needs 🌱
# 📥 Inputs: Age group, lactose & gluten allergy status, meal preference, and plan requirement.
# 📤 Outputs: Customized dietary recommendations and detailed gluten-free meal plans.
# _______________________________________________________________________________________________
# _______________________________________________________________________________________________
from experta import *
import random

# Define a class to store user profile information
class UserProfile(Fact):
    """Info about the user's dietary and lifestyle preferences."""
    pass

# Define the SafeBiteEngine that will provide recommendations based on user profile
class SafeBiteEngine(KnowledgeEngine):

    # Define rules for providing recommendations when plan='yes'
    @Rule(UserProfile(plan='yes', age='children', lactose_gluten_allergy='yes', meal_preference='light'))
    def rule_1(self):
        self.add_recommendations('children', 'light', 'yes')
        self.add_meal_plan('children', 'light')

    @Rule(UserProfile(plan='yes', age='children', lactose_gluten_allergy='yes', meal_preference='main'))
    def rule_2(self):
        self.add_recommendations('children', 'main', 'yes')
        self.add_meal_plan('children', 'main')

    @Rule(UserProfile(plan='yes', age='children', lactose_gluten_allergy='no', meal_preference='light'))
    def rule_3(self):
        self.add_recommendations('children', 'light', 'no')
        self.add_meal_plan('children', 'light')

    @Rule(UserProfile(plan='yes', age='children', lactose_gluten_allergy='no', meal_preference='main'))
    def rule_4(self):
        self.add_recommendations('children', 'main', 'no')
        self.add_meal_plan('children', 'main')

    @Rule(UserProfile(plan='yes', age='adults', lactose_gluten_allergy='yes', meal_preference='light'))
    def rule_5(self):
        self.add_recommendations('adults', 'light', 'yes')
        self.add_meal_plan('adults', 'light')

    @Rule(UserProfile(plan='yes', age='adults', lactose_gluten_allergy='yes', meal_preference='main'))
    def rule_6(self):
        self.add_recommendations('adults', 'main', 'yes')
        self.add_meal_plan('adults', 'main')

    @Rule(UserProfile(plan='yes', age='adults', lactose_gluten_allergy='no', meal_preference='light'))
    def rule_7(self):
        self.add_recommendations('adults', 'light', 'no')
        self.add_meal_plan('adults', 'light')

    @Rule(UserProfile(plan='yes', age='adults', lactose_gluten_allergy='no', meal_preference='main'))
    def rule_8(self):
        self.add_recommendations('adults', 'main', 'no')
        self.add_meal_plan('adults', 'main')

    @Rule(UserProfile(plan='yes', age='aged', lactose_gluten_allergy='yes', meal_preference='light'))
    def rule_9(self):
        self.add_recommendations('aged', 'light', 'yes')
        self.add_meal_plan('aged', 'light')

    @Rule(UserProfile(plan='yes', age='aged', lactose_gluten_allergy='yes', meal_preference='main'))
    def rule_10(self):
        self.add_recommendations('aged', 'main', 'yes')
        self.add_meal_plan('aged', 'main')

    @Rule(UserProfile(plan='yes', age='aged', lactose_gluten_allergy='no', meal_preference='light'))
    def rule_11(self):
        self.add_recommendations('aged', 'light', 'no')
        self.add_meal_plan('aged', 'light')

    @Rule(UserProfile(plan='yes', age='aged', lactose_gluten_allergy='no', meal_preference='main'))
    def rule_12(self):
        self.add_recommendations('aged', 'main', 'no')
        self.add_meal_plan('aged', 'main')

    # Define Rules 13 and 14 for plan='no'
    @Rule(UserProfile(plan='no', age='children', lactose_gluten_allergy='yes', meal_preference='light'))
    def rule_13(self):
        self.add_recommendations_no_plan('children', 'light', 'yes')

    @Rule(UserProfile(plan='no', age='children', lactose_gluten_allergy='yes', meal_preference='main'))
    def rule_14(self):
        self.add_recommendations_no_plan('children', 'main', 'yes')

    # Existing methods for plan='yes'
    def add_recommendations(self, age, meal_preference, lactose_gluten_allergy):
        # Add recommendations based on age group
        if age == 'children':
            self.recommendations.append("- Ensure meals are nutrient-dense to support growth and development.")
            self.recommendations.append(
                "- Include a variety of fruits, vegetables, whole grains, and protein-rich foods.")
        elif age == 'adults':
            self.recommendations.append("- Maintain a balanced diet to support overall health and energy levels.")
            self.recommendations.append("- Incorporate a mix of macronutrients and micronutrients in your diet.")
        elif age == 'aged':
            self.recommendations.append("- Focus on foods that are easy to digest and rich in vitamins and minerals.")
            self.recommendations.append("- Ensure adequate intake of calcium, vitamin D, and fiber.")

        # Add recommendations based on meal preference
        if meal_preference == 'light':
            self.recommendations.append("- Opt for lighter meals like salads, soups, and smoothies.")
            self.recommendations.append("- Avoid heavy, calorie-dense foods that may cause discomfort.")
        elif meal_preference == 'main':
            self.recommendations.append(
                "- Include balanced main meals with a source of protein, carbohydrates, and healthy fats.")
            self.recommendations.append("- Ensure portions are adequate to meet your energy needs.")

        # Add recommendations for lactose and gluten allergies
        if lactose_gluten_allergy == 'yes':
            self.recommendations.append("- Avoid dairy and gluten-containing products.")
            self.recommendations.append(
                "- Opt for lactose-free alternatives like almond milk or coconut yogurt, and gluten-free grains like quinoa and rice.")

    def add_meal_plan(self, age, meal_preference):
        meal_plan = {
            'children': {
                'light': {
                    'breakfast': "Oatmeal with almond milk and berries.",
                    'lunch': "Grilled chicken salad with mixed greens and a light vinaigrette.",
                    'dinner': "Vegetable soup with gluten-free bread."
                },
                'main': {
                    'breakfast': "Scrambled eggs with gluten-free toast and a side of fruit.",
                    'lunch': "Chicken and quinoa bowl with steamed vegetables.",
                    'dinner': "Baked fish with sweet potatoes and green beans."
                }
            },
            'adults': {
                'light': {
                    'breakfast': "Green smoothie with spinach, banana, and almond milk.",
                    'lunch': "Quinoa salad with chickpeas, cucumber, and tomatoes.",
                    'dinner': "Stir-fried vegetables with tofu."
                },
                'main': {
                    'breakfast': "Greek yogurt with gluten-free granola and honey.",
                    'lunch': "Grilled chicken breast with brown rice and steamed broccoli.",
                    'dinner': "Beef stir-fry with bell peppers and quinoa."
                }
            },
            'aged': {
                'light': {
                    'breakfast': "Chia pudding with almond milk and sliced fruit.",
                    'lunch': "Lentil soup with a side salad.",
                    'dinner': "Baked zucchini with quinoa stuffing."
                },
                'main': {
                    'breakfast': "Omelet with spinach and mushrooms.",
                    'lunch': "Baked salmon with roasted vegetables.",
                    'dinner': "Chicken stew with carrots and potatoes."
                }
            }
        }

        selected_meal_plan = meal_plan[age][meal_preference]
        self.recommendations.append("\n🍴 Detailed Daily Gluten-Free Meal Plan: 🍴")
        self.recommendations.append(f"- Breakfast: {selected_meal_plan['breakfast']}")
        self.recommendations.append(f"- Lunch: {selected_meal_plan['lunch']}")
        self.recommendations.append(f"- Dinner: {selected_meal_plan['dinner']}")

    # New method to add recommendations when plan='no'
    def add_recommendations_no_plan(self, age, meal_preference, lactose_gluten_allergy):
        self.recommendations.append(
            "🤖 Here are your personalized gluten-free recommendations based on your profile: 🤖")

        # Add general recommendations based on age group
        if age == 'children':
            self.recommendations.append("- Ensure your child receives a balanced diet with essential nutrients.")
            self.recommendations.append(
                "- Include a variety of fruits, vegetables, whole grains, and protein-rich foods.")
        elif age == 'adults':
            self.recommendations.append("- Maintain a balanced diet rich in fruits, vegetables, and whole grains.")
            self.recommendations.append("- Incorporate a mix of macronutrients and micronutrients in your diet.")
        elif age == 'aged':
            self.recommendations.append("- Focus on foods that are easy to digest and rich in vitamins and minerals.")
            self.recommendations.append("- Ensure adequate intake of calcium, vitamin D, and fiber.")

        # Add recommendations based on meal preference
        if meal_preference == 'light':
            self.recommendations.append("- Opt for lighter meal options such as salads and soups.")
            self.recommendations.append("- Avoid heavy, calorie-dense foods that may cause discomfort.")
        elif meal_preference == 'main':
            self.recommendations.append(
                "- Include balanced main meals with a source of protein, carbohydrates, and healthy fats.")
            self.recommendations.append("- Ensure portions are adequate to meet your energy needs.")

        # Add recommendations for lactose and gluten allergies
        if lactose_gluten_allergy == 'yes':
            self.recommendations.append("- Avoid dairy and gluten-containing products.")
            self.recommendations.append(
                "- Opt for lactose-free alternatives like almond milk or coconut yogurt, and gluten-free grains like quinoa and rice.")

    # Constructor to initialize the engine and recommendations list
    def __init__(self):
        super().__init__()
        self.recommendations = []


# Function to get valid user input
def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input. Please enter one of the following: {', '.join(valid_options)}")


if __name__ == "__main__":
    # Print welcome message to the user
    print("=" * 100)
    print("=" * 100)
    print("{:^100}".format("✨ Welcome to SafeBite! ✨"))
    print("=" * 100)
    print("=" * 100)
    print(
        "👋 Welcome to SafeBite! We specialize in providing gluten-free and safe meal options that suit your lifestyle. 🍽️")
    print("💪 Our goal is to provide personalized nutritional plans that promote healthy living. 💪")
    print("🌱 Let's create a healthy and nutritious journey for you! 🌱")
    print("=" * 100)

    # Initialize the SafeBite engine
    engine = SafeBiteEngine()
    engine.reset()

    # Get user profile information from input
    age = get_valid_input("Enter age group (children, adults, aged): ", ['children', 'adults', 'aged'])
    lactose_gluten_allergy = get_valid_input("Do you have lactose intolerance along with gluten allergy? (yes/no): ",
                                             ['yes', 'no'])
    plan = get_valid_input("Do you need a nutritional plan? (yes/no): ", ['yes', 'no'])
    meal_preference = get_valid_input("Do you prefer light meals or main meals? (light/main): ", ['light', 'main'])

    # Declare user profile fact to the engine
    engine.declare(
        UserProfile(age=age, lactose_gluten_allergy=lactose_gluten_allergy, plan=plan, meal_preference=meal_preference))
    print("\n\n" + "-" * 60)
    if plan == 'yes':
        print(
            "🌿 Below is a specially tailored gluten-free meal plan that suits your dietary needs and preferences. 🌿\n")
        print("🤖 Here are your personalized gluten-free recommendations based on your profile: 🤖\n")


    engine.run()

    # Print personalized recommendations
    if engine.recommendations:
        for recommendation in engine.recommendations:
            print(recommendation)
    else:
        print("- No recommendations available based on your profile.")

    # Print thank you message
    print("\n" + "=" * 100)
    print("=" * 100)
    print("{:^100}".format("🙏 Thank you for using SafeBite! 🙏"))
    print("{:^100}".format("🎉 We hope this plan helps you enjoy nutritious and safe meals every day. 🎉"))
    print("{:^100}".format("🥳 Stay healthy and take care! 🥳"))
    print("=" * 100)
    print("=" * 100)
