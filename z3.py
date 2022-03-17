#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def min_laboratories(**kwargs):
    """ Минимальное количество сданных работ по ОПИ

    На вход поступает имя студента и количество сданных работ

    Функция выводит студента с наименьшим количеством работ

    """
    if kwargs:
        min_labs = min(kwargs.values())
        for student, labs in kwargs.items():
            if labs == min_labs:
                print(
                    f"The least laboratories ({labs}) "
                    f"has the student: {student}"
                )
    else:
        return None


if __name__ == "__main__":
    min_laboratories(Elena=6, Dima=12, Oleg=3, Trofim=7)
    min_laboratories(Sasha=9, Vitya=15, Aleksey=14)
    min_laboratories(Efim=13)