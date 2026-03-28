"""
Title: Storage Efficiency of Can Sizes Calculator
Author: Clinton Jake Cai
Description: Computes the storage efficiency of can sizes by calculating the volume and the surface area.
"""
import math
from pathlib import Path

def main():
    dir = Path(__file__).parent
    file_path = dir / "can_list_info.txt"
    with open(file_path, "r") as can_list_file:
        for can_info in can_list_file:
            can_info = [item.strip() for item in can_info.strip().split(",")]
            # Alternate: can_info = can_info.strip().split(", ")
            
            can_name = can_info[0]
            can_radius = float(can_info[1])
            can_height = float(can_info[2])
            can_cost = (can_info[3])
            
            volume = compute_volume(can_radius, can_height)
            surface_area = compute_surface_area(can_radius, can_height)
            storage_efficiency = compute_storage_efficiency(volume, surface_area)
            
            print(f"{can_name}: Radius = {can_radius:.2f} | Height = {can_height:.2f} | Cost = {can_cost} | Volume = {volume:.2f} | Surface Area = {surface_area:.2f} | Storage Efficiency = {storage_efficiency:.2f}")
            
def compute_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume
    
def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency
main()