from bing_images import bing

bing.download_images("cars from brand 'smart'",
                      100,
                      pool_size=30,
                      force_replace=True)