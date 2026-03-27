# Contact Tracing Using Ball-Tree Algorithm

High-performance spatial contact tracing using Ball Tree data structures -- published in IEEE Xplore.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python) ![scikit-learn](https://img.shields.io/badge/scikit--learn-BallTree-F7931E?style=flat-square&logo=scikitlearn) ![pandas](https://img.shields.io/badge/pandas-Data-150458?style=flat-square&logo=pandas) ![IEEE](https://img.shields.io/badge/IEEE-Published-00629B?style=flat-square&logo=ieee)

## What It Does

This project implements contact tracing using the Ball Tree spatial data structure for efficient nearest-neighbor queries on large-scale location datasets. It handles 10,000+ data points with sub-linear query time, making it suitable for real-world contact tracing scenarios. The research behind this implementation has been published in IEEE Xplore.

## Key Features

- **Ball Tree Nearest Neighbor Search** -- efficient spatial queries with sub-linear time complexity
- **Scales to 10,000+ Data Points** -- handles large datasets without performance degradation
- **Proximity Detection** -- configurable distance and time thresholds for contact identification
- **Matplotlib Visualizations** -- visual contact maps and spatial distribution plots
- **CSV Export** -- structured output of detected contact pairs
- **IEEE Published** -- peer-reviewed research backing the implementation

## Tech Stack

| Category | Technologies |
|----------|-------------|
| Language | Python 3.x |
| Spatial Indexing | scikit-learn BallTree |
| Data Processing | pandas, NumPy |
| Visualization | Matplotlib |
| Performance | Cython, C extensions |

## Getting Started

```bash
git clone https://github.com/Jesseman-418/Contact-Tracing-using-Ball-tree-Algorithm.git
cd Contact-Tracing-using-Ball-tree-Algorithm
pip install scikit-learn pandas numpy matplotlib
python3 main.py
```

## Publication

This work has been published in **IEEE Xplore**. The Ball-tree approach provides improved query performance over traditional brute-force methods for high-dimensional contact tracing data.

## Related Work

See also: [Contact Tracing using KD-Tree Algorithm](https://github.com/Jesseman-418/contact_tracing_using_kd-tree_algorithm) -- the KD-Tree variant of this approach.

## License

MIT
