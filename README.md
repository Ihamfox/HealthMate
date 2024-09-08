# HealthMate
#### Video Demo:  <(https://youtu.be/0RbhJVhpb6c)>
#### Description:
HealthMate is an innovative web application developed as the final project for my CS50 course, it offers users an intuitive platform for tracking and managing their health metrics, specifically Body Mass Index (BMI), Basal Metabolic Rate (BMR), and macronutrient intake. The application integrates a suite of web technologies to deliver an interactive experience.

- Technical Implementation and Features:

**Core Calculations:** HealthMate’s functionality centers around precise calculations for BMI, BMR, and macronutrient needs. Users input their weight, height, age, gender, and daily activity , and the application performs the necessary calculations.

**BMI Calculation:** Users provide their weight and height, and HealthMate computes their BMI using a straightforward formula. The application then categorizes the result into standard weight ranges, aiding users in understanding their weight status, BMI= weight / (height)² This calculation provides users with a numerical value that falls into specific categories, such as underweight, normal weight, overweight, or obesity.

**BMR Calculation:** HealthMate calculates the Basal Metabolic Rate based on user-provided details using established formulas. This calculation determines the number of calories required to maintain basic bodily functions at rest, which is essential for tailoring dietary plans.

**Macronutrient Tracking:** Users input their age , gender , weight , height and activity level , and HealthMate calculates the required grams of proteins, fats, and carbohydrates based on their chosen distribution percentages. This feature helps users maintain a balanced diet by providing detailed macronutrient targets.

**User Accounts and Data Management:** A key feature of HealthMate is its user account system. This allows users to create personal accounts where they can save and track their health data over time. By registering, users can:

Save Health Metrics: Store their BMI, BMR, and weight records securely.
Track Progress: View historical data and trends, enabling them to monitor changes and make informed adjustments to their health strategies.
Ensure Data Security: Access their data safely with user-specific login credentials.
The account system is built using Flask’s user authentication features, with secure password hashing and session management to ensure data protection.

- Technical Stack and Development: HealthMate was developed using a combination of modern technologies and frameworks:

**Python and Flask:** Python serves as the primary programming language, leveraging Flask for the server-side logic and routing. Flask’s flexibility allows for the easy integration of various components and functionalities, including handling user requests and processing health calculations.

**Jinja Templating:** Jinja is used for dynamic HTML rendering. It allows for efficient management of website templates, with a base layout.html file extended across multiple pages. This approach ensures consistency in design and simplifies updates.

**HTML and CSS:** HTML structures the web pages, while CSS styles the elements to create a visually appealing and user-friendly interface. CSS files are used to define the layout, typography, and interactive elements, enhancing the overall user experience.

**SQLite:** SQLite serves as the database management system for storing user data and health metrics in the database.db file . Its integration with Flask enables efficient data operations and ensures that the application remains responsive and reliable.

- Application Structure: The application is organized into several key folders:

**Templates Folder:** Contains HTML files for each page, utilizing Jinja templating to extend a common layout and ensure uniformity across the site.
**Static Folder:** Houses the CSS files that style the application, contributing to its modern and responsive design.
**Projects Folder:** Includes app.py, the core of the application where Flask routes and handlers are defined. This file integrates the calculations, manages user interactions, and interfaces with the SQLite database.

**User Experience and Interface:** HealthMate emphasizes a user-friendly design with intuitive navigation. The interface is designed to be responsive, ensuring compatibility across various devices and screen sizes. The clean and modern design facilitates easy access to key features, such as entering health data, viewing results, and managing account settings.

HealthMate represents a significant achievement in my journey through the CS50 course, demonstrating my ability to integrate various technologies into a cohesive and functional web application. By offering accurate calculations for BMI, BMR, and macronutrient needs, along with the ability to save and track personal health data, The project not only highlights my technical skills but also reflects my commitment to creating practical solutions that support users in achieving their health goals.

Thank you so much CS50 , This was CS50  <3

                                            Hamed Khalifa