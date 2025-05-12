# 🌍 Interactive Seismic Activity Dashboard

![Seismic Dashboard Banner](img/earthquakeappbanner.png)

## 🖼️ Dashboard Banner Artwork
This project's dashboard banner was generated using **Stable Diffusion** with a custom prompt to visually represent seismic activity in a futuristic interface. No text or labels were included to keep it clean and versatile for any display.

### 🎨 Prompt Used
A futuristic dashboard with a glowing 3D world map showing earthquake epicenters. Neon orange and blue seismic charts, dynamic heatmaps, aligned UI elements, no text. Dark cyberpunk city background with holograms. Ultra-detailed, high-tech, ambient lighting, 4K.

### 🧪 Generation Settings
- **Prompt**: 
- **Seed**: `2314`
- **Steps**: `90`
- **Resolution**: `4K`
- **Sampler**: DPM++ 2M Karras (recommended)
- **Model**: Stable Diffusion 1.5 or SDXL (for higher detail)
- **Refiner (optional)**: Yes, for sharper UI elements and alignment

### 🛠️ How to Recreate It
You can recreate a similar image using the same prompt and settings in any of the following tools:
- 🖥️ **Automatic1111 WebUI**
- 🌐 **HuggingFace Diffusers + `torch`**
- 🧠 **InvokeAI**
- 🧪 **ComfyUI**

Make sure to:
- Use a seed (`2314`) for deterministic output
- Disable any watermark or text overlays
- Keep CFG scale around `7.0` to `9.0` for prompt adherence

> This image is free to use within the scope of this project. Attribution appreciated but not required.

## Overview

**Interactive Seismic Activity Dashboard** is a modern, interactive web application for exploring and analyzing global seismic activity. Built with [Streamlit](https://streamlit.io/) and [Plotly](https://plotly.com/), it enables users to visualize, filter, and interpret earthquake data for a complete month, with advanced analytics and clustering.

---

## 🚀 Features

- **Dynamic Filtering:**  
  Filter seismic events by date, magnitude, depth, event type, and region.
- **Rich Visualizations:**  
  - 📊 General summary metrics and distributions
  - 🌐 Interactive maps and heatmaps
  - ⏱️ Temporal evolution and patterns
  - 📈 Advanced correlation and comparative analysis
- **Cluster Analysis:**  
  Identify spatial clusters of seismic events using DBSCAN.
- **Downloadable Data:**  
  Export filtered datasets as CSV.
- **Responsive UI:**  
  Wide layout, expandable tables, and interpretation hints.

---

## 🛠️ Tech Stack

- **Python 3.8+**
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Plotly Express & Graph Objects](https://plotly.com/python/)
- [scikit-learn](https://scikit-learn.org/)
- [Matplotlib](https://matplotlib.org/)

---

## 📂 Project Structure

```
earthquakes_app/
│
├── app.py                         # Main Streamlit dashboard
├── data/
│   └── all_month.csv              # Seismic data (CSV)
├── img/
│   └── earthquakeappbanner.png    # Banner
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

---

## ⚡ Quick Start

1. **Clone the repository:**
    ```sh
    git clone https://github.com/patriciajaquez/earthquakes_app.git
    cd earthquakes_app
    ```

2. **Install dependencies:**
    ```sh
    python -m venv earthquakesenv
    source earthquakesenv/bin/activate
    pip install -r requirements.txt
    ```

3. **Add your data:**  
   Place your `all_month.csv` file in the `data/` directory.

4. **Run the app:**
    ```sh
    streamlit run app.py
    ```

5. **Open in browser:**  
   Visit [http://localhost:8501](http://localhost:8501) to interact with the dashboard.

---

## 📊 Example Screenshots

| General Summary | Geographic Map | Cluster Analysis |
|:--------------:|:-------------:|:---------------:|
| ![Summary](https://img.icons8.com/color/48/summary-list.png) | ![Map](https://img.icons8.com/color/48/worldwide-location.png) | ![Cluster](https://img.icons8.com/color/48/cluster.png) |

---

## 🧩 Data Format

The dashboard expects a CSV file (`all_month.csv`) with at least the following columns:

- `id`, `time`, `updated`, `latitude`, `longitude`, `depth`, `mag`, `place`, `type`, `magType`, `rms`, etc.

> **Tip:** Download recent earthquake data from [USGS Earthquake Catalog](https://earthquake.usgs.gov/earthquakes/search/).

---

## 📚 How It Works

- **Data Loading:**  
  Loads and preprocesses data, removing timezones and adding derived columns (day, hour, week, magnitude category).
- **Filtering:**  
  Sidebar widgets allow multi-criteria filtering in real time.
- **Visualization:**  
  Uses Plotly for interactive charts and maps, including scatter plots, histograms, bar charts, and heatmaps.
- **Clustering:**  
  DBSCAN algorithm groups events by spatial proximity, visualized on the map and with summary tables.
- **Analysis Tabs:**  
  Organized into tabs for summary, geographic, temporal, and advanced analyses.

---

## 📝 Customization

- **Change color schemes:**  
  Edit the `magnitude_colors` dictionary in `app.py`.
- **Add new analyses:**  
  Extend the dashboard by adding new tabs or charts using Streamlit and Plotly.

---

## 🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🌐 Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/)
- [USGS Earthquake Catalog](https://earthquake.usgs.gov/)

---

> 📚 Created as part of the Data Analytics and AI Bootcamp by [Patricia Jaquez](https://github.com/patriciajaquez). This project demonstrates practical applications of data visualization and analysis techniques.
