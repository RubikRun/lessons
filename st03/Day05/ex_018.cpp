// Exercise 18:
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
// When the mouse is in the right half of the window, the circles should be red.
// Otherwise they should be blue.
//
// To know where the mouse is you can use this variable "mouse".
// Typing "mouse.x" gives you the X coordinate of the mouse in the current frame,
// and typing "mouse.y" gives you the Y coordinate of the mouse.
//
// By default this drawCircle() function draws a red circle.
// If you want to draw a blue circle you can give it an RGB color at the end, like that:
//     drawCircle(50, 50, 8, {30, 30, 190});
//
// (See ex_018.mp4)
//
void render(sf::Vector2i mouse)
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

        const sf::Vector2i mousePos = sf::Mouse::getPosition(window);
        render(mousePos);

        // Update the window
        window.display();
    }
}