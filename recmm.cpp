#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

class MovieRecommendationSystem {
private:
    map<string, vector<int>> userPreferences; // User preferences for movies

public:
    void addUserPreferences(const string& username, const vector<int>& movieRatings) {
        userPreferences[username] = movieRatings;
    }

    double calculateSimilarity(const vector<int>& user1, const vector<int>& user2) {
        double dotProduct = 0.0;
        double normUser1 = 0.0;
        double normUser2 = 0.0;

        for (size_t i = 0; i < user1.size(); ++i) {
            dotProduct += user1[i] * user2[i];
            normUser1 += pow(user1[i], 2);
            normUser2 += pow(user2[i], 2);
        }

        double similarity = dotProduct / (sqrt(normUser1) * sqrt(normUser2));
        return similarity;
    }

    vector<int> getRecommendations(const string& username) {
        vector<int> recommendations;

        for (const auto& entry : userPreferences) {
            const string& otherUser = entry.first;
            if (otherUser != username) {
                double similarity = calculateSimilarity(userPreferences[username], entry.second);

                // Arbitrary threshold for similarity
                if (similarity > 0.5) {
                    recommendations.insert(recommendations.end(), entry.second.begin(), entry.second.end());
                }
            }
        }

        // Remove duplicates from recommendations
        sort(recommendations.begin(), recommendations.end());
        recommendations.erase(unique(recommendations.begin(), recommendations.end()), recommendations.end());

        return recommendations;
    }
};

int main() {
    MovieRecommendationSystem recommendationSystem;

    // Simulate adding user preferences
    recommendationSystem.addUserPreferences("User1", {5, 3, 0, 4, 0});
    recommendationSystem.addUserPreferences("User2", {0, 4, 5, 0, 3});
    recommendationSystem.addUserPreferences("User3", {3, 0, 0, 2, 5});

    // Get movie recommendations for a user
    vector<int> recommendedMovies = recommendationSystem.getRecommendations("User1");

    // Display recommended movies
    cout << "Recommended movies for User1:" << endl;
    for (int movieId : recommendedMovies) {
        cout << "Movie " << movieId << endl;
    }

    return 0;
}
