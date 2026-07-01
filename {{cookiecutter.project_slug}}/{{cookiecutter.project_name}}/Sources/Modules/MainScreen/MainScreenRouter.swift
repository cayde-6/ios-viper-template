//
//  MainScreenRouter.swift
//  {{ cookiecutter.project_name }}
//
//  Created by {{ cookiecutter.author_name }}.
//

import UIKit

protocol MainScreenRouter { }

final class MainScreenRouterImpl {
    weak var navigationController: UINavigationController?

    init(navigationController: UINavigationController?) {
        self.navigationController = navigationController
    }
}

extension MainScreenRouterImpl: MainScreenRouter { }
