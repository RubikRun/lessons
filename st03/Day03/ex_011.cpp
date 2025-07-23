// Exercise 11:
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
// so that it draws 2 circles:
// - first one must be at position x = 100, y = 200, and have radius of 50
// - second one must be at position x = 300, y = 300, and have radius of 120
//
// How to do that?
// You can use the drawCircle(...) function.
// The way it works is you give it 3 numbers:
// - The X position of your circle
// - The Y position of your circle
// - The radius of your circle
// and it will draw the circle.
// For example
//     drawCircle(200, 100, 30)
// will draw a circle at position x = 200, y = 100 with radius of 30.
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