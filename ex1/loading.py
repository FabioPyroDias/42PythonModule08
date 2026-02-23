import sys
import importlib


if __name__ == "__main__":
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")
    packages = ["numpy", "pandas", "requests", "matplotlib"]
    modules = {}
    errors = []
    for package in packages:
        try:
            # importlib.import_module - Import a module dinamically
            # The use of this method in this way, allows the program
            # to detect if such dependencies were correctly installed
            module = importlib.import_module(package)
            modules[package] = module
            if module.__name__ == "pandas":
                print(f"[OK] {module.__name__} ({module.__version__}) "
                      f"- Data manipulation ready")
            elif module.__name__ == "requests":
                print(f"[OK] {module.__name__} ({module.__version__}) "
                      f"- Network access ready")
            elif module.__name__ == "matplotlib":
                print(f"[OK] {module.__name__} ({module.__version__}) "
                      f"- Visualization ready")
        except (ImportError) as e:
            errors.append(f"[ERROR] {e}")
    if len(errors) > 0:
        for error in errors:
            print(error)
        sys.exit()
    print()
    print("Analyzing Matrix data...")
    try:
        request = (modules["requests"]
                   .get('https://randomuser.me/api/?results=1000'))
        if request.status_code != 200:
            raise ValueError("Requests could not get data")
        print("Processing 1000 data points...")
        # Get 1000 random samples using requests
        samples = modules["pandas"].DataFrame(request.json()["results"])
        # Filter to get specific desired data
        data = [sample["street"]["number"] for sample in samples["location"]]
        modules["matplotlib"] = importlib.import_module("matplotlib.pyplot")
        print("Generating visualization...")
        # Creation of the plot (graphic)
        plot = (modules["matplotlib"]
                .plot(modules["numpy"].arange(1, 1001, 1), data))
        modules["matplotlib"].title("Street Number Distribution")
        modules["matplotlib"].xlabel("Count")
        modules["matplotlib"].ylabel("Street Number")
        modules["matplotlib"].savefig(f"{sys.prefix}/_analysis.png")
        print()
        print("Analysis complete!")
        print("Results saved to: matrix\\_analysis.png}")
    except (ValueError, ConnectionError) as e:
        print(f"Error: {e}")
