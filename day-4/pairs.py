from dataclasses import dataclass
from enum import Enum


@dataclass
class ElfSectors:
    start: int
    end: int


class SectorOverlap(Enum):
    ALL = 0
    PARTIAL = 1


def get_part_one_answer(pairs_sectors):
    amount_of_pairs = 0
    for pairs in pairs_sectors:
        splitted = pairs.split(",")
        first_elf, second_elf = splitted[0], splitted[1]
        if first_elf_sectors_in_second_elfs_sectors(first_elf, second_elf, SectorOverlap.ALL) or \
           second_elf_sectors_in_first_elfs_sectors(first_elf, second_elf, SectorOverlap.ALL):
                amount_of_pairs += 1

    return amount_of_pairs


def get_part_two_answer(pairs_sectors):
    amount_of_pairs = 0
    for pairs in pairs_sectors:
        splitted = pairs.split(",")
        first_elf, second_elf = splitted[0], splitted[1]
        if first_elf_sectors_in_second_elfs_sectors(first_elf, second_elf, SectorOverlap.PARTIAL) or \
           second_elf_sectors_in_first_elfs_sectors(first_elf, second_elf, SectorOverlap.PARTIAL):
                amount_of_pairs += 1

    return amount_of_pairs


def first_elf_sectors_in_second_elfs_sectors(first_elf_sectors, second_elf_sectors, overlap: SectorOverlap):
    first_elf = get_elf_sector_start_and_end(first_elf_sectors)
    second_elf = get_elf_sector_start_and_end(second_elf_sectors)

    if overlap is SectorOverlap.ALL:
        return second_elf.start <= first_elf.start <= second_elf.end and \
               second_elf.start <= first_elf.end <= second_elf.end

    if overlap is SectorOverlap.PARTIAL:
        return second_elf.start <= first_elf.start <= second_elf.end or \
               second_elf.start <= first_elf.end <= second_elf.end


def second_elf_sectors_in_first_elfs_sectors(first_elf_sectors, second_elf_sectors, overlap: SectorOverlap):
    first_elf = get_elf_sector_start_and_end(first_elf_sectors)
    second_elf = get_elf_sector_start_and_end(second_elf_sectors)

    if overlap is SectorOverlap.ALL:
        return first_elf.start <= second_elf.start <= first_elf.end and \
               first_elf.start <= second_elf.end <= first_elf.end

    if overlap is SectorOverlap.PARTIAL:
        return first_elf.start <= second_elf.start <= first_elf.end or \
               first_elf.start <= second_elf.end <= first_elf.end


def get_elf_sector_start_and_end(elf):
    splitted = elf.split("-")
    first_elf_sector_start = int(splitted[0])
    first_elf_sector_end = int(splitted[1])

    return ElfSectors(first_elf_sector_start, first_elf_sector_end)


def main():
    pairs_ids = open("assignment_pairs.txt", "r", encoding="utf8").readlines()

    print("part one answer:", get_part_one_answer(pairs_ids))
    print("part two answer:", get_part_two_answer(pairs_ids))


if __name__ == '__main__':
    main()
