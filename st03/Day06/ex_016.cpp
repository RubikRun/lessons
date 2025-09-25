// Exercise 16:
// Look below

#include <SFML/Graphics.hpp>

static sf::RenderWindow window;

// Wrapper function to draw a circle at (x, y) with given radius
void drawCircle(int x, int y, int radius, sf::Color color = {190, 30, 30}) {
    sf::CircleShape circle(radius);
    circle.setFillColor(color);

    // SFML positions the shape by the top-left of its bounding box,
    // so to center it at (x, y), we move its origin to its center
    circle.setOrigin({float(radius), float(radius)});
    circle.setPosition({float(x), float(y)});

    window.draw(circle);
}



// Fill in this render() function
// so that it draws a big rectangle made out of small circles.
//
// Coordinates used in image:
//     Top-left circle at:
//           x = 200
//           y = 100
//       Bottom-right circle at:
//           x = 600
//           y = 500
//       Offset between circles:
//           20 in both x and y
//       Radius of a circle:
//           8
//
// (See ex_016.png)
//
void render()
{
}




int main()
{
    // Create the main window
    sf::ContextSettings settings;
    settings.antiAliasingLevel = 16;
    window = sf::RenderWindow(sf::VideoMode({800, 600}), "SFML window", sf::Style::Default, sf::State::Windowed, settings);

    // Start the game loop
    while (window.isOpen())
    {
        // Process events
        while (const std::optional event = window.pollEvent())
        {
            // Close window: exit
            if (event->is<sf::Event::Closed>())
                window.close();
        }
 
        // Clear screen
        window.clear();

        render();

        // Update the window
        window.display();
    }
}