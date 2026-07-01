//
//  MainScreenPresenter.swift
//  {{ cookiecutter.project_name }}
//
//  Created by {{ cookiecutter.author_name }}.
//

import Foundation

@MainActor
protocol MainScreenPresenter {
    var viewModel: MainScreenViewModel { get }
    func onAppear()
}

@MainActor
final class MainScreenPresenterImpl {
    let viewModel: MainScreenViewModel
    private let router: MainScreenRouter

    init(viewModel: MainScreenViewModel, router: MainScreenRouter) {
        self.viewModel = viewModel
        self.router = router
    }
}

extension MainScreenPresenterImpl: MainScreenPresenter {
    func onAppear() {
        print("🎯 MainScreenPresenter: onAppear")
    }
}
