#include <SFML/Graphics.hpp>

static sf::RenderWindow window;

// Wrapper function to draw a circle at (x, y) with given radius
void drawCircle(int x, int y, int radius, sf::Color color = {190, 30, 30})
{
    sf::CircleShape circle(radius);
    circle.setFillColor(color);

    // SFML positions the shape by the top-left of its bounding box,
    // so to center it at (x, y), we move its origin to its center
    circle.setOrigin({float(radius), float(radius)});
    circle.setPosition({float(x), float(y)});

    window.draw(circle);
}

void drawRectangle(int x, int y, int width, int height, sf::Color color = {30, 190, 30})
{
    sf::RectangleShape rect({float(width), float(height)});
    rect.setFillColor(color);

    // SFML positions shapes from their top-left corner,
    // so we set the origin to the rectangle's center
    rect.setOrigin({float(width) / 2.f, float(height) / 2.f});
    rect.setPosition({float(x), float(y)});

    window.draw(rect);
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

bool upPressed()
{
    return sf::Keyboard::isKeyPressed(sf::Keyboard::Key::Up);
}

bool downPressed()
{
    return sf::Keyboard::isKeyPressed(sf::Keyboard::Key::Down);
}




// Now that we have the two paddles,
// let's draw the ball in the center of the screen
// and make it move.
//
// For now it will not bounce off the paddles or walls,
// it will just move diagonally up-right.
//
// Hint: you can use either drawCircle() or drawRectangle() to draw the ball, your choice.
void render()
{
}


int main()
{
    // Create the main window
    sf::ContextSettings settings;
    settings.antiAliasingLevel = 16;
    window = sf::RenderWindow(sf::VideoMode({1400, 800}), "SFML window", sf::Style::Default, sf::State::Windowed, settings);
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