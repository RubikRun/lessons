#include <SFML/Graphics.hpp>
#include <optional>

#include <random>
#include <vector>

using namespace sf;

const int WINDOW_WIDTH = 1280;
const int WINDOW_HEIGHT = 720;

RenderWindow window;

// Gives you a random number
// between some min and max values (including min and max)
int randomInt(int min, int max)
{
    static std::random_device rd;
    static std::mt19937 rng(rd());
    std::uniform_int_distribution<int> dist(min, max);

    return dist(rng);
}

// Gives you a random color
sf::Color randomColor()
{
    return sf::Color(
        randomInt(0, 255),
        randomInt(0, 255),
        randomInt(0, 255)
    );
}

// Draws a circle
void drawCircle(int x, int y, int radius, Color color)
{
    CircleShape circle = CircleShape(float(radius));
    circle.setFillColor(color);

    // SFML positions shapes by their top-left corner.
    // This centers the circle on (x, y)
    circle.setPosition({ float(x) - float(radius), float(y) - float(radius) });

    window.draw(circle);
}








void initialize()
{
}

void render()
{
}






int main()
{
    ContextSettings contextSettings;
    contextSettings.antiAliasingLevel = 8;

    window = RenderWindow(VideoMode({ WINDOW_WIDTH, WINDOW_HEIGHT }), "Empty Graphics Project", Style::Default, State::Windowed, contextSettings);
    window.setFramerateLimit(60);

    initialize();

    while (window.isOpen())
    {
        while (const std::optional event = window.pollEvent())
        {
            if (event->is<Event::Closed>())
                window.close();
        }

        window.clear(Color::Black);

        render();

        window.display();
    }

    return 0;
}