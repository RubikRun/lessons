// Exercise 23:
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

// Returns true if the W key is pressed, and false otherwise.
bool wPressed()
{
    return sf::Keyboard::isKeyPressed(sf::Keyboard::Key::W);
}

// Returns true if the A key is pressed, and false otherwise.
bool aPressed()
{
    return sf::Keyboard::isKeyPressed(sf::Keyboard::Key::A);
}

// Returns true if the S key is pressed, and false otherwise.
bool sPressed()
{
    return sf::Keyboard::isKeyPressed(sf::Keyboard::Key::S);
}

// Returns true if the D key is pressed, and false otherwise.
bool dPressed()
{
    return sf::Keyboard::isKeyPressed(sf::Keyboard::Key::D);
}




// Fill in this render() function
// so that it draws a blue circle (any size, any position).
// The circle should turn red whenever the W key is pressed.
//
// You can use the wPressed() function - look at it above.
//
// This is how you draw a blue circle:
//     drawCircle(..., sf::Color::Blue);
// This is how you draw a red circle:
//     drawCircle(..., sf::Color::Red);
void render()
{
}


int main()
{
    // Create the main window
    sf::ContextSettings settings;
    settings.antiAliasingLevel = 16;
    window = sf::RenderWindow(sf::VideoMode({800, 600}), "SFML window", sf::Style::Default, sf::State::Windowed, settings);
    window.setFramerateLimit(60);

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