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




// We'll make the classic pong game!
// If you don't know what it is, you can play it here:
//     https://freepong.org/
// Description of the game:
//     The game has two paddles and a ball. The paddles can move up and down to hit the ball back and forth.
//     The left paddle is controlled with W and S.
//     The right paddle is controlled with the Up and Down arrow keys.
//     The ball moves automatically, bouncing off the top and bottom of the screen.
//     If the ball goes past a paddle, the other player scores a point.
//
// Let's start with the left paddle.
// We'll draw it as a rectangle on the left side of the screen,
// and move it up and down with W and S.
// Fill in the render function below to implement this.
//
// Hint: use drawRectangle() to draw the paddle.
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