// Exercise 14:
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
// so that it draws 40 circles, each one with radius 8,
// at positions:
//     x = 20, y = 20
//     x = 40, y = 40
//     x = 60, y = 60
//     x = 80, y = 80
//     ...
//     x = 780, y = 780
//     x = 800, y = 800
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