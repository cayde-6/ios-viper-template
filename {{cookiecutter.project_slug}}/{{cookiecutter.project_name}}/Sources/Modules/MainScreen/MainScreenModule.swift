//
//  MainScreenModule.swift
//  {{ cookiecutter.project_name }}
//
//  Created by {{ cookiecutter.author_name }}.
//

import UIKit

protocol MainScreenModule { }

final class MainScreenModuleImpl {
    static func build(
        navigationController: UINavigationController? = nil
    ) -> MainScreenView {
        // Create ViewModel
        let viewModel = MainScreenViewModel()

        // Create Router
        let router = MainScreenRouterImpl(navigationController: navigationController)

        // Create Presenter
        let presenter = MainScreenPresenterImpl(
            viewModel: viewModel,
            router: router
        )

        // Return assembled view
        return MainScreenView(
            viewModel: viewModel,
            presenter: presenter
        )
    }
}

extension MainScreenModuleImpl: MainScreenModule { }
