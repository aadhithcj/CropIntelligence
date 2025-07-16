interface PredictionRequest {
  year?: number;
  rainfall: number;
  monsoon?: number;
  score?: number;
  district: string;
}

interface PredictionResponse {
  predicted_crop: string;
  confidence: number;
  input_params: {
    year: number;
    rainfall: number;
    monsoon: number;
    score: number;
    district: string;
  };
  yieldPotential?: number;
  soilType?: string;
  temperature?: number;
  rainfall?: number;
}

const API_BASE_URL = 'http://localhost:5000/api';

export const predictBestCrop = async (data: PredictionRequest): Promise<PredictionResponse> => {
  try {
    const response = await fetch(`${API_BASE_URL}/predict`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.error('Error predicting crop:', error);
    throw error;
  }
};

export const getWeatherData = async (lat: number, lng: number) => {
  try {
    // For now, return simulated data that matches Kerala climate
    const simulatedWeather = {
      temperature: 26 + Math.random() * 6,
      humidity: 70 + Math.random() * 25,
      rainfall: Math.random() * 5,
      windSpeed: 8 + Math.random() * 12,
      pressure: 1008 + Math.random() * 10,
      visibility: 6 + Math.random() * 4,
      condition: ['sunny', 'cloudy', 'rainy', 'partly-cloudy'][Math.floor(Math.random() * 4)] as 'sunny' | 'cloudy' | 'rainy' | 'partly-cloudy',
      uvIndex: 5 + Math.random() * 6,
      description: 'Partly cloudy with chance of rain'
    };
    
    return simulatedWeather;
  } catch (error) {
    console.error('Error fetching weather data:', error);
    throw error;
  }
};

export const checkHealth = async (): Promise<{ status: string; models_loaded: boolean }> => {
  try {
    const response = await fetch(`${API_BASE_URL}/health`);
    return await response.json();
  } catch (error) {
    console.error('Error checking health:', error);
    throw error;
  }
};